class Musica:
    # método construtor: executado automaticamente quando criamos uma nova música
    def __init__(self, titulo, artista, duracao_seg, arte_disco="♫"):
        self.titulo = titulo # armazena o nome da música
        self.artista = artista # armazena o nome do cantor ou banda
        self.duracao_seg = duracao_seg # armazena a duração total em segundas inteiras
        
        # símbolo ou pequeno texto de 3 caracteres para o rótulo da musica
        self.arte_disco = arte_disco[:3].center(3)
        
    # método auxiliar para converter os segundos totais no formato visual tradicional "MM:SS".
    def formatar_duracao(self):
        minutos = self.duracao_seg // 60
        segundos = self.duracao_seg % 60
        return f"{minutos:02d}:{segundos:02d}"

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.formatar_duracao()})"
