
from django.db import models

class Team(models.Model): #seznam týmů
    name = models.CharField(max_length=100, default='neznámé')  # Název klubu
    city = models.CharField(max_length=100, default='neznámé')  # Město
    stadium = models.CharField(max_length=100, default='neznámé')  # Stadion

    def __str__(self):
        return self.name


class Chart(models.Model): # tabulka
    team = models.ForeignKey(Team, on_delete=models.CASCADE) # Tento cizí klíč (ForeignKey) odkazuje na jiný model Team. Spojení konkrétním týmem.on_delete=models.CASCADE znamená, že pokud bude tým, na který tento cizí klíč odkazuje, smazán, všechny odpovídající záznamy v modelu Chart budou také smazány.
    position = models.IntegerField()
    matches_played = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.position}" # při jeho zobrazení se ukáže název týmu a jeho pozice (např. "Sparta - 1").


class Player(models.Model):  # hráči
    POSITION_CHOICES = [
        ('B', 'Brankář'),
        ('O', 'Obránce'),
        ('Z', 'Záložník'),
        ('Ú', 'Útočník'),
    ]
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)  # Odkaz na tým
    number = models.IntegerField()  # Číslo dresu
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default='neznámé')  # Pozice
    country = models.CharField(max_length=50, default='neznámé')  # Země
    name = models.CharField(max_length=100, default='neznámé')  # Jméno hráče

    def __str__(self):
        return f"{self.number}. {self.position} {self.name} ({self.country})"
