import subprocess
import time
from pathlib import Path

SIMHUB_EXE = r"C:\Program Files (x86)\SimHub\SimHubWPF.exe"
SIMHUB_PLUGINS_DATA = r"C:\Program Files (x86)\SimHub\PluginsData"

ARQUIVO_TXT = "shortcuts.txt"

TEMPO_CARREGAR_SIMHUB = 20
TEMPO_APOS_TROCAR_JOGO = 3
INTERVALO_ENTRE_PROGRAMAS = 1


def limpar_linha(linha):
    return linha.strip().strip('"').strip("'")


def abrir_exe(caminho_exe):
    caminho = Path(caminho_exe)

    if not caminho.exists():
        print(f"Arquivo não encontrado: {caminho_exe}")
        return False

    print(f"Abrindo: {caminho_exe}")

    subprocess.Popen(
        [str(caminho)],
        cwd=str(caminho.parent)
    )

    return True


def abrir_simhub():
    caminho = Path(SIMHUB_EXE)

    if not caminho.exists():
        print(f"SimHub não encontrado em: {SIMHUB_EXE}")
        return False

    print("Abrindo SimHub...")

    subprocess.Popen(
        [str(caminho)],
        cwd=str(caminho.parent)
    )

    return True


def jogo_existe_no_simhub(nome_jogo):
    pasta_jogo = Path(SIMHUB_PLUGINS_DATA) / nome_jogo
    return pasta_jogo.exists()


def trocar_jogo_simhub(nome_jogo):
    if not jogo_existe_no_simhub(nome_jogo):
        print(f"Aviso: não encontrei uma pasta do jogo no SimHub com o nome: {nome_jogo}")
        print(f"Confira os nomes em: {SIMHUB_PLUGINS_DATA}")
        print("Vou tentar enviar o comando mesmo assim...")

    print(f"Trocando jogo no SimHub para: {nome_jogo}")

    try:
        subprocess.run(
            [
                SIMHUB_EXE,
                "-switchgame",
                nome_jogo
            ],
            cwd=str(Path(SIMHUB_EXE).parent),
            timeout=10
        )

        print("Comando enviado ao SimHub.")

    except subprocess.TimeoutExpired:
        print("O comando de troca demorou demais e foi encerrado pelo Python.")

    except Exception as e:
        print(f"Erro ao trocar jogo no SimHub: {e}")

    time.sleep(TEMPO_APOS_TROCAR_JOGO)


def carregar_txt():
    arquivo = Path(ARQUIVO_TXT)

    if not arquivo.exists():
        print(f"Arquivo TXT não encontrado: {ARQUIVO_TXT}")
        return None, []

    with open(arquivo, "r", encoding="utf-8-sig") as f:
        linhas = f.readlines()

    linhas_validas = []

    for linha in linhas:
        linha_limpa = limpar_linha(linha)

        if not linha_limpa:
            continue

        if linha_limpa.startswith("#"):
            continue

        linhas_validas.append(linha_limpa)

    if not linhas_validas:
        print("O arquivo TXT está vazio ou só possui comentários.")
        return None, []

    jogo_simhub = linhas_validas[0]
    programas = linhas_validas[1:]

    return jogo_simhub, programas


def executar_macro():
    jogo_simhub, programas = carregar_txt()

    if not jogo_simhub:
        return

    if not abrir_simhub():
        return

    inicio_simhub = time.time()

    # Enquanto o SimHub carrega, já abre os outros programas
    for programa in programas:
        abrir_exe(programa)
        time.sleep(INTERVALO_ENTRE_PROGRAMAS)

    # Calcula quanto tempo ainda falta para completar os 20 segundos
    tempo_passado = time.time() - inicio_simhub
    tempo_restante = TEMPO_CARREGAR_SIMHUB - tempo_passado

    if tempo_restante > 0:
        print(f"Aguardando mais {tempo_restante:.1f} segundos antes de trocar o jogo no SimHub...")
        time.sleep(tempo_restante)

    trocar_jogo_simhub(jogo_simhub)

    print("Macro finalizada. O Python será encerrado, mas os programas continuam abertos.")


if __name__ == "__main__":
    executar_macro()


#------------- Game names for the .txt file -------------#
#
#         "American Truck Simulator",
#         "Assetto Corsa (PC only)",
#         "Assetto Corsa Competizione (PC only)",
#         "Assetto Corsa EVO (PC only)",
#         "Assetto Corsa Rally",
#         "Automobilista",
#         "Automobilista 2",
#         "BeamNG",
#         "BMW M3 Challenge",
#         "Copa Petrobras de Marcas",
#         "Dirt Showdown",
#         "Dirt 3",
#         "Dirt Rally (PC only)",
#         "Dirt Rally 2.0 (PC only)",
#         "Dirt 4",
#         "Euro Truck Simulator 2",
#         "Farming Simulator 19",
#         "Farming Simulator 22",
#         "Farming Simulator 25",
#         "TML Fernbus Simulator",
#         "TML Tourist Bus Simulator",
#         "Codemasters Dirt 2",
#         "Codemasters F1 2012",
#         "Codemasters F1 2013",
#         "Codemasters F1 2014",
#         "Codemasters F1 2015",
#         "Codemasters F1 2016",
#         "Codemasters F1 2017",
#         "Codemasters F1 2018 (PC + Consoles)",
#         "Codemasters F1 2019 (PC + Consoles)",
#         "Codemasters F1 2020 (PC + Consoles)",
#         "Codemasters F1 2021 (PC + Consoles)",
#         "Codemasters F1 22 (PC + Consoles)",
#         "Codemasters F1 23 (PC + Consoles)",
#         "Codemasters F1 24 (PC + Consoles)",
#         "Codemasters F1 25 (PC + Consoles)",
#         "Codemasters Grid 2",
#         "Codemasters Grid (2019)",
#         "Codemasters Grid Autosport",
#         "Codemasters Grid Legends",
#         "Drift21",
#         "EA WRC (PC)",
#         "eXpanSIM",
#         "Formula Truck 2013",
#         "Forza Horizon 4 (PC + Consoles)",
#         "Forza Horizon 5 (PC + Consoles)",
#         "Forza Horizon 6 (PC + Consoles)",
#         "Forza Motorsport 7",
#         "Forza Motorsport 8",
#         "FURIDASHI: Drift Cyber Sport",
#         "GP Bikes (Piboso)",
#         "Gran Turismo Sport (PS4)",
#         "Gran Turismo 7 (PS4, PS5)",
#         "GT Legends",
#         "GTR",
#         "GTR 2",
#         "GRally",
#         "HydroSim",
#         "iRacing",
#         "Kart Racing Pro (Piboso)",
#         "KartKraft",
#         "Le Mans Ultimate",
#         "Live For Speed",
#         "MotoGP 18",
#         "Nascar Heat 4",
#         "Nascar Heat 5",
#         "NASCAR Racing: 2003 Season",
#         "NoLimits 2",
#         "OMSI 2",
#         "Piboso MX Bikes",
#         "Project Cars (PC only)",
#         "Project Cars 2 (PC + Consoles)",
#         "Project Cars 3",
#         "Project Motor Racing",
#         "Race 07",
#         "Raceroom",
#         "RDS – The Official Drift Videogame",
#         "Richard Burns Rally",
#         "RFactor",
#         "RFactor 2",
#         "SimBin Race The WTCC Game",
#         "SRX: The Game",
#         "Test Drive Unlimited Solar Crown",
#         "TML The Bus",
#         "Tony Stewart’s All-American Racing",
#         "Tony Stewart’s Sprint Car Racing",
#         "Trackmania 2 Series",
#         "Trackmania Turbo",
#         "Game Stock Car Extreme",
#         "Volvo The Game",
#         "WRC 7/8/9",
#         "WRC 10",
#         "WRC Generations",
#         "Wreckfest 2",
#     "Flight simulators":
#         "Condor 3",
#         "Condor 2",
#         "DCS",
#         "Elite Dangerous **",
#         "Flight Simulator 2020",
#         "Flight Simulator 2024",
#         "IL-2 Sturmovik",
#         "X-Plane 10",
#         "X-Plane 11",
#         "X-Plane 12",
#         "War Thunder *",
#         "Aces Of Thunder (PC only) *",
#     "Others":
#         "Counter Strike 2 ***",
#         "Dota 2 ***",
#         "Epic Roller Coasters",
#         "Kayak VR Mirage **",
#         "NoLimits 2",
#         "Train Simulator 2021 ***",
