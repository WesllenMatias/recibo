import sqlite3
import pprint
from reportlab.pdfgen import canvas

class GeraRecibo:
    
    con = sqlite3.connect('recibo.db')
    c = con.cursor()
    
    

    def cadastro_empresa(self):
        #self.id = 1
        #self.id_empresa += self.id
        self.empresa = input("Informe a Empresa: ")
        self.razao_social = input("Informe a Razão Social: ")
        self.cnpj = input("Informe o CNPJ: ")
        self.end_empresa = input("Informe o Endereço: ")
        
             
        GeraRecibo.con
        GeraRecibo.c.execute("""
        INSERT INTO cad_empresa (empresa,razao,cnpj,endereco) VALUES (
            ?,
            ?,
            ?,
            ?
        )
        """, (self.empresa,self.razao_social,self.cnpj,self.end_empresa))
        GeraRecibo.con.commit()
        GeraRecibo.con.close()
        
    def gerapdf(self):
        cnpj_recibo = input("Informe o CNPJ da Empresa Cadastrada: ")
        cpf_prestador = input("Informe o CPF do Prestador Cadastrado: ")
        serv = input("Informe o Serviço Prestado: ")
        vlr = input("Informe o Valor do Serviço Prestado: ")
        GeraRecibo.con
        GeraRecibo.c.execute("""SELECT razao,cnpj,empresa FROM cad_empresa WHERE cnpj = ?""", [cnpj_recibo])
        GeraRecibo.c.execute("""SELECT nome_prestador,cpf,identidade,data_nasc,nome_mae FROM cad_prestador WHERE cpf = ?""", [cpf_prestador])
        emp = GeraRecibo.c.fetchone()
        pprint.pprint(emp)
        arquivo = str(emp[2])
        pdf = canvas.Canvas("{}-{}.pdf".format(arquivo,))
        self.texto_rec = "Recebi da(o) " + str(emp[0]) +", CNPJ: "+ str(emp[1]) + ","
        self.texto_rec2 = "a importância de R$ {} pela prestação de serviços referentes a:".format(vlr)
        self.texto_rec3 ="{}.".format(serv)
        pdf.setFont('Courier-Bold', 20)
        pdf.drawCentredString(300,770,"Recibo de Pagamento de Autônomo - RPA")
        pdf.line(30,750,550,750)
        pdf.setFont('Courier', 12)
        pdf.setTitle("Recibo")
        pdf.drawString(50,680, self.texto_rec)
        pdf.drawString(50,660, self.texto_rec2)
        pdf.drawString(50,640, self.texto_rec3)
        pdf.line(30,750,550,750)
        pdf.save()
        
    def cadastro_prestador(self):
        self.nome = input("Informe o Nome Completo do Prestador de Serviço:")
        self.cpf = input("Informe o CPF:")
        self.identidade = input("Informe o Número da Identidade:")
        self.orgao_emissor = input("Informe o Orgão Emissor da Identidade:")
        self.n_pis = input("Informe o Número do PIS:")
        self.dt_nasc = input("Informe a Data de Nascimento:")
        self.n_mae = input("Nome da Mãe:")
        self.end_prest = input("Endereço:")
        
        GeraRecibo.con
        GeraRecibo.c.execute("""
        INSERT INTO cad_prestador (nome_prestador,cpf,identidade,emissor,data_nasc,nome_mae,endereco_prestador) VALUES (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )
        """, (self.nome,self.cpf,self.identidade,self.orgao_emissor,self.dt_nasc,self.n_mae,self.end_prest))
        GeraRecibo.con.commit()
        GeraRecibo.con.close()

    def listar_cad_empresa(self):
        GeraRecibo.con
        for linha in GeraRecibo.c.execute("SELECT empresa,razao,cnpj FROM cad_empresa"):
            pprint.pprint(linha)
                        
        GeraRecibo.con.close()
        
    def listar_cad_prestador(self):
        GeraRecibo.con
        for linha in GeraRecibo.c.execute("SELECT nome_prestador,cpf,identidade FROM cad_prestador"):
            pprint.pprint(linha)
            
        GeraRecibo.con.close()        

#GeraRecibo().cadastro_empresa()
#GeraRecibo().cadastro_prestador()
GeraRecibo().gerapdf()
#GeraRecibo().listar_cad_empresa()
#GeraRecibo().listar_cad_prestador()




#    referente=input("O Recibo é Referente:")
#    valor_b=input("Valor bruto do recibo:")
#    valor_l=input("Valor liquido do recibo:")
#    inss = input("Valor descontado INSS:")
#    irrf = input("Valor descontado IRRF:")
#    iss = input("Valor descontado ISS")