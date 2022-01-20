import tabula
import os

file = "bb0121_tac_at.pdf"

tabula.convert_into(file, "aprovados.csv", output_format="csv", pages="all", delimiter=";")
