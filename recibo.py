import sqlite3
from reportlab.pdfgen import canvas

class GeraRecibo:
    
    con = sqlite3.connect('recibo.db')
    c = con.cursor()
    
    pdf = canvas.Canvas("nome_do_pdf.pdf")

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
        a = GeraRecibo()
        print(self.razao_social)
        #self.texto_rec = "Recebi da(o) " + a.razao_social +", CNPJ: "+ a.cnpj + ","
        #self.texto_rec2 = "a importância de R$ XXXX,XX pela prestação de serviços referentes a:"
        #self.texto_rec3 ="XXXXXXXXX XXXX XXXXXX."
        #GeraRecibo.pdf.setFont('Courier-Bold', 20)
        #GeraRecibo.pdf.drawCentredString(300,770,"Recibo de Pagamento de Autônomo - RPA")
        #eraRecibo.pdf.line(30,750,550,750)
        #GeraRecibo.pdf.setFont('Courier', 12)
        #GeraRecibo.pdf.setTitle("Recibo")
        #GeraRecibo.pdf.drawString(50,680, self.texto_rec)
        #eraRecibo.pdf.drawString(50,660, self.texto_rec2)
        #eraRecibo.pdf.drawString(50,640, self.texto_rec3)
        #GeraRecibo.pdf.line(30,750,550,750)
        #GeraRecibo.pdf.save()
        
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
        INSERT INTO cad_empresa (nome_prestador,cpf,identidade,emissor,data_nascimento,nome_mae,endereco_prestador) VALUES (
            ?,
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


GeraRecibo().cadastro_empresa()
#GeraRecibo().cadastro_prestador()
#GeraRecibo().gerapdf()




#    referente=input("O Recibo é Referente:")
#    valor_b=input("Valor bruto do recibo:")
#    valor_l=input("Valor liquido do recibo:")
#    inss = input("Valor descontado INSS:")
#    irrf = input("Valor descontado IRRF:")
#    iss = input("Valor descontado ISS")