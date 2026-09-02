"""Testes do servidor MCP do diário — exercitam as regras sem subir o protocolo.

O decorador @mcp.tool() devolve a função original, então cada ferramenta é
chamada aqui como função Python comum.
"""
import shutil

import pytest

import servidor
from mcp.server.mcpserver.exceptions import ToolError


@pytest.fixture(autouse=True)
def csv_isolado(tmp_path, monkeypatch):
    """Copia o CSV real para tmp e aponta o servidor para lá — testes não mexem no arquivo versionado."""
    copia = tmp_path / "turma.csv"
    shutil.copy(servidor.ARQUIVO, copia)
    monkeypatch.setattr(servidor, "ARQUIVO", copia)
    return copia


# --- regras de cálculo -------------------------------------------------------

def test_media_ponderada():
    assert servidor._media({"n1": "6.0", "n2": "7.0", "n3": "8.5"}) == 7.3


def test_media_incompleta_quando_falta_nota():
    assert servidor._media({"n1": "6.0", "n2": "7.0", "n3": ""}) is None


@pytest.mark.parametrize(
    "media, esperado",
    [(None, "incompleto"), (7.0, "aprovado"), (6.99, "exame"), (5.0, "exame"), (4.99, "reprovado")],
)
def test_situacao(media, esperado):
    assert servidor._situacao(media) == esperado


def test_buscar_matricula_inexistente_levanta_toolerror():
    with pytest.raises(ToolError, match="nao existe na turma"):
        servidor._buscar([], "9999999")


# --- ferramentas -----------------------------------------------------------

def test_boletim_aluno_aprovado():
    saida = servidor.boletim("2024001")
    assert "Ana Maria Silva (2024001)" in saida
    assert "situacao: aprovado" in saida


def test_listar_alunos_traz_a_turma_toda():
    saida = servidor.listar_alunos()
    for matricula in ("2024001", "2024002", "2024003", "2024004", "2024005"):
        assert matricula in saida


def test_resumo_turma_conta_por_situacao(csv_isolado):
    csv_isolado.write_text(
        "matricula,nome,n1,n2,n3\n"
        "1,A,8.0,8.0,8.0\n"   # aprovado
        "2,B,8.0,8.0,8.0\n"   # aprovado
        "3,C,5.0,5.0,5.0\n"   # exame
        "4,D,2.0,2.0,2.0\n"   # reprovado
        "5,E,7.0,7.0,\n",     # incompleto
        encoding="utf-8",
    )
    saida = servidor.resumo_turma()
    assert "turma: 5 alunos" in saida
    assert "aprovado: 2 | exame: 1 | reprovado: 1 | incompleto: 1" in saida


def test_lancar_nota_valida_persiste_e_descreve_o_efeito():
    saida = servidor.lancar_nota("2024004", 3, 8.5)
    assert "7.3" in saida and "aprovado" in saida
    assert "8.5" in servidor.boletim("2024004")


def test_lancar_nota_fora_da_faixa_recusa_e_nao_grava():
    antes = servidor.ARQUIVO.read_text(encoding="utf-8")
    with pytest.raises(ToolError, match="nota invalida: 11.0"):
        servidor.lancar_nota("2024005", 2, 11.0)
    assert servidor.ARQUIVO.read_text(encoding="utf-8") == antes


def test_lancar_nota_avaliacao_inexistente_recusa():
    with pytest.raises(ToolError, match="avaliacao deve ser 1, 2 ou 3"):
        servidor.lancar_nota("2024005", 4, 7.0)


# --- recurso -------------------------------------------------------------

def test_recurso_regras_descreve_pesos_e_limites():
    texto = servidor.regras()
    assert "N1=3, N2=3, N3=4" in texto
    assert "aprovado: media >= 7.0" in texto
