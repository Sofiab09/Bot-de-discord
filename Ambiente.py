import discord 


def etiqueta_reducción():
    embed = discord.Embed(
        title= "1. Reducción de residuos",
        description= "Descubre como reducir la cantidad de residuos que generas con estos consejos practicos",
        color= 0x00aaff,
    )
    embed.add_field(
        name="Evita plásticos desechables: ",
        value= "Usa bolsas reutilizables, botellas de agua de acero inoxidable, y utensilios de bambú o metálicos.",
        inline= False
    )
    embed.add_field(
        name="Compra a granel: ",
        value= "Lleva tus propios frascos o bolsas para comprar granos, especias, y productos frescos.",
        inline= False
    )
    embed.set_thumbnail(
        url= "https://i.postimg.cc/Sxvw7nc8/eco-1.jpg"
    )
    return embed

def etiqueta_reutilizarReciclar():
    embed = discord.Embed(
        title= "2. Ideas para reutilizar y reciclar",
        description= "Inspirate con estas ideas para darle una nueva vida a tus objetos",
        color= 0x32CD32,
    )
    embed.add_field(
        name="Envases de vidrio: ",
        value= "Úsalos como recipientes para alimentos, macetas pequeñas o lámparas decorativas.",
        inline= False
    )
    return embed

def etiqueta_consumoResponsable():
    embed = discord.Embed(
        title= "3. Consumo Responsable",
        description= "Tomar decisiones responsables para reducir el impacto ambiental",
        color= 0xFFA500,
    )
    embed.add_field(
        name="Investiga marcas:",
        value= "Compra a empresas que promuevan prácticas éticas, paguen salarios justos y usen materiales sostenibles.",
        inline= False
    )
    return embed

