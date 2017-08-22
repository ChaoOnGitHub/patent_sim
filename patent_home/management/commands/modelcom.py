from patent_home.models import LSIModel
import cPickle
from gensim import corpora,similarities




def modelcommand():
    dictionary_path = '/Users/zhanghc/PycharmProjects/django_data_product_v2.0/patent_sim/patent_data.dict'
    dictionary = corpora.Dictionary.load(dictionary_path)
    index = similarities.MatrixSimilarity.load('./LSIsim.index')
    LSI_model_object =LSIModel.objects.order_by("-run_date").first()
    model            =cPickle.loads(LSI_model_object.models_pickle)

    return dictionary,index,model