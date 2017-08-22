from django.core.management.base import BaseCommand
import datetime
from patent_home.models import LSIModel
from pytz import timezone
from django.conf import settings
import cPickle
from gensim import corpora,models,similarities

class Command(BaseCommand):
    help = "Create LSI model for patent claim text."

    def handle(self, *args, **options):
        # Load dictionary and corpus
        dictionary_path    = '/Users/zhanghc/PycharmProjects/django_data_product_v2.0/patent_sim/patent_data.dict'
        corpus_path        = '/Users/zhanghc/PycharmProjects/django_data_product_v2.0/patent_sim/patent_data.mm'

        # Create LSI model
        dictionary         =corpora.Dictionary.load(dictionary_path)
        corpus             =corpora.MmCorpus(corpus_path)
        LSI                =models.LsiModel(corpus,id2word=dictionary,num_topics=10)
        index              =similarities.MatrixSimilarity(LSI[corpus])
        index.save('./LSIsim.index')
        run_date           =datetime.datetime.now(tz=timezone(settings.TIME_ZONE))


        # Save model
        lsi_model_object   =LSIModel.objects.create(models_pickle=cPickle.dumps(LSI),
                                                    run_date     =run_date)

