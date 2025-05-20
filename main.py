#importa o arquivo que contem a classe contabancaria
from poo3 import ContaBancaria

conta_um = ContaBancaria("Thyago Lannes",1000)
conta_um.consultar_saldo()

conta_um.depositar(200)
conta_um.consultar_saldo()