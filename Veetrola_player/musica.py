class Musica:
    def __init__(self, titulo, artista, duracao_seg, arte_disco="♫"):
        self.titulo = titulo
        self.artista = artista
        self.duracao_seg = duracao_seg
        # símbolo ou pequeno texto de 3 caracteres para o rótulo do vinil
        self.arte_disco = arte_disco[:3].center(3)

    def formatar_duracao(self):
        minutos = self.duracao_seg // 60
        segundos = self.duracao_seg % 60
        return f"{minutos:02d}:{segundos:02d}"

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.formatar_duracao()})"
