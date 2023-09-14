from django.db import models
from stdimage.models import StdImageField

# Signals -> utilizado para executar algum recurso antes ou depois de uma ação no BD
from django.db.models import signals

# Slug -> recurso que faz a URL trazer o título-da-pagina-separado-por-tracos-e-em-minusculas
from django.template.defaultfilters import slugify

# Uma classe de apoio, poderia ter outro nome, como Util, Apoio...
# Por ser uma classe abstrata, não é gerado nada no BD
class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


# captura a instância de produto, usa o nome do produto para ser o slug (vide comentário no import)
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


# Antes de salvar um Produto, disparar o método produto_pre_save
signals.pre_save.connect(produto_pre_save, sender=Produto)



