import os
import time


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def _desenhar_vitrola(musica, deslocamento=0, tocando=True, status_extra=""):
    """
    Desenha os comandos no topo e a vitrola com o disco no centro.
    'deslocamento' move o disco horizontalmente para animar a entrada/saída.
    """
    limpar_tela()
    print("=" * 68)
    print(" COMANDOS: [P] Play/Pause | [N] Próxima | [B] Anterior | [F] Fila")
    print("           [S] Buscar     | [A] Catálogo| [+] Nova     | [T] Carga | [0] Sair")
    print("=" * 68)

    if musica is None:
        print("\n              [ Nenhuma música carregada na vitrola ]\n")
        return

    simbolo = musica.arte_disco
    estado = "▶ TOCANDO" if tocando else "❚❚ PAUSADO"
    braco = "  \\  " if tocando else "   | "
    ponta_braco = "   O " if tocando else "   | "

    # Espaçamento lateral para simular o disco entrando/saindo da bandeja
    pad = " " * deslocamento

    print(f"\n  Status: {estado} {status_extra}")
    print(f"  Faixa : {musica.titulo} — {musica.artista} [{musica.formatar_duracao()}]")
    print("  +------------------------------------------------------------+")
    print(f"  | {pad}        . - ~ ~ ~ - .        {braco}                  |")
    print(f"  | {pad}    . '   . - ~ - .   ' .    {ponta_braco}                  |")
    print(f"  | {pad}  /     . '  [{simbolo}]  ' .     \\   |                   |")
    print(f"  | {pad} |     |     ( o )     |     |  |                   |")
    print(f"  | {pad}  \\     ' .  {simbolo}  . '     /  /                    |")
    print(f"  | {pad}    ' .   ' - _ - '   . '  o                     |")
    print(f"  | {pad}        ' - _ _ _ - '                            |")
    print("  +------------------------------------------------------------+")


def animar_troca_disco(musica_antiga, musica_nova, tocando=True):
    """Anima o disco antigo saindo para a direita e o novo entrando pela esquerda."""
    if musica_antiga is not None:
        for passo in (2, 6, 12, 18):
            _desenhar_vitrola(musica_antiga, deslocamento=passo, tocando=False, status_extra="(Ejetando disco...)")
            time.sleep(0.06)

    if musica_nova is not None:
        for passo in (18, 12, 6, 2, 0):
            _desenhar_vitrola(musica_nova, deslocamento=passo, tocando=False, status_extra="(Carregando disco...)")
            time.sleep(0.06)
        _desenhar_vitrola(musica_nova, deslocamento=0, tocando=tocando)


def renderizar_tela(musica, tocando, fila, pilha):
    _desenhar_vitrola(musica, deslocamento=0, tocando=tocando)
    print("\n  [ PRÓXIMAS NA FILA (FIFO) ]")
    print(fila.listar_elementos())
    print("\n  [ ÚLTIMAS TOCADAS - HISTÓRICO (LIFO) ]")
    print(pilha.listar_elementos(limite=3))
    print("-" * 68)
