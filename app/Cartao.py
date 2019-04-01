import os
import sys
import slugify
from PIL import Image, ImageFont, ImageDraw, ImageFilter


class Cartao(object):

    app_folder = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, c_width=500, c_height=135, bg_color=(255, 255, 255),
                 f_color=(23, 103, 200), logo="img/Logo-Stefani.jpg",
                 fs_name=16, fs_office=14, fs_paragraph=12,
                 f_name="Roboto-Bold.ttf", f_office="Roboto-Regular.ttf",
                 ft_paragraph="Roboto-Bold.ttf", f_paragraph="Roboto-Regular.ttf"):
        self.c_width = c_width
        self.c_height = c_height
        self.bg_color = bg_color
        self.logo = logo
        self.f_color = f_color
        self.fs_name = fs_name
        self.fs_office = fs_office
        self.fs_paragraph = fs_paragraph
        self.f_name = f_name
        self.f_office = f_office
        self.ft_paragraph = ft_paragraph
        self.f_paragraph = f_paragraph

        self.check_files()

    def check_files(self):
        print("*** Verificando Arquivos de Fontes ***")
        if not os.path.exists(os.path.join(self.app_folder, "fonts")):
            print("Pasta de Fontes não existe!.")
            sys.exit(1)
        elif not os.path.exists(os.path.join(self.app_folder, "fonts", self.f_name)):
            print("Fonte do Nome não existe. %s" % self.f_name)
            sys.exit(1)
        elif not os.path.exists(os.path.join(self.app_folder, "fonts", self.f_office)):
            print("Fonte do Cargo não existe. %s" % self.f_office)
            sys.exit(1)
        elif not os.path.exists(os.path.join(self.app_folder, "fonts", self.ft_paragraph)):
            print("Fonte do Titulo do Paragrafo não existe. %s" %
                  self.ft_paragraph)
            sys.exit(1)
        elif not os.path.exists(os.path.join(self.app_folder, "fonts", self.f_paragraph)):
            print("Fonte do Paragrafo não existe. %s" % self.f_paragraph)
            sys.exit(1)
        elif not os.path.exists(os.path.join(self.app_folder, self.logo)):
            print("Imagem da Logo não existe. %s" % self.logo)
            sys.exit(1)
        else:
            print("Tudo certo, Continuando! \n\n")
            return True

    def _get_logo(self):
        """
        Pega a Logo da Empresa
        """
        logo = Image.open(os.path.join(self.app_folder, self.logo))
        logo = logo.resize((190, 65), Image.ANTIALIAS)
        return logo

    def _get_fonts(self):
        """
        Pega a Fonte da Empresa
        """
        fontBold = ImageFont.truetype(os.path.join(self.app_folder, "fonts", self.f_name), self.fs_name)
        fontBNormal = ImageFont.truetype(os.path.join(self.app_folder, "fonts", self.f_office), self.fs_office)
        fontNormal = ImageFont.truetype(os.path.join(self.app_folder, "fonts", self.ft_paragraph), self.fs_paragraph)
        fontNBold = ImageFont.truetype(os.path.join(self.app_folder, "fonts", self.f_paragraph), self.fs_paragraph)
        return fontBold, fontBNormal, fontNormal, fontNBold

    def nome_saida(self, filename, saida):
        """ gera o nome da saida com o nome do funcionario """
        new_filename = slugify.slugify(filename)+'.jpg'
        return os.path.join(self.app_folder, saida, new_filename)

    def gerar(self, cell, saida):
        """
        Gera Cartão
        """
        img = Image.new('RGB', (self.c_width, self.c_height), self.bg_color)
        draw = ImageDraw.Draw(img)

        nome, cargo, titulo, paragrafo = self._get_fonts()

        # Adicionando Logo
        logo = self._get_logo()
        img.paste(logo, (4, 35))

        # Adicionando Linhas
        draw.line([(205, 5), (205, 130)], fill=self.f_color)
        draw.line([(215, 50), (490, 50)], fill=self.f_color)

        # Nome e Cargo
        draw.text((215, 8), cell[0].value, self.f_color, font=nome)
        draw.text((215, 29), cell[1].value, self.f_color, font=cargo)

        # Resto das Informações
        draw.text((215, 55), "Phone:", self.f_color, font=titulo)
        draw.text((280, 55), "+55 (16) 3209-4788",
                  self.f_color, font=paragrafo)

        draw.text((215, 73), "Email:", self.f_color, font=titulo)
        draw.text((280, 73), cell[2].value,
                  self.f_color, font=paragrafo)

        if cell[3].value is None:
            draw.text((215, 91), "Facebook:",
                      self.f_color, font=titulo)
            draw.text((280, 91), "facebook.com/ceramicastefanisa",
                      self.f_color, font=paragrafo)
        else:
            draw.text((215, 91), "Skype:", self.f_color,
                      font=titulo)
            draw.text((280, 91), cell[3].value,
                      self.f_color, font=paragrafo)
            draw.text((215, 109), "Facebook:",
                      self.f_color, font=titulo)
            draw.text((280, 109), "facebook.com/ceramicastefanisa",
                      self.f_color, font=paragrafo)

        if not os.path.exists(os.path.join(self.app_folder, saida)):
            os.mkdir(os.path.join(self.app_folder, saida))

        img.save(self.nome_saida(cell[2].value, saida))
