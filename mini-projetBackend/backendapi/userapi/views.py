from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .models import User 
from .serializers import UserSerializer
from django.core.files.storage import FileSystemStorage
from keras.preprocessing import image
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
import numpy as np
import pandas as pd 





with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        modelApple = load_model('./models/apple_model.h5',compile=False)

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        modelTomato= load_model('./models/model_tomate_4epocs.h5',compile=False)

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        modelStrawberry=load_model('./models/model_fraise.h5',compile=False)

treatment_tomato={
0:"How can I prevent bacterial spot in the future? Plant pathogen-free seed or transplants to prevent the introduction of bacterial spot pathogens on contaminated seed or seedlings.  If a clean seed source is not available or you suspect that your seed is contaminated, soak seeds in water at 122 F for 25 min. to kill the pathogens.  To keep leaves dry and to prevent the spread of the pathogens, avoid overhead watering (e.g., with a wand or sprinkler) of established plants and instead use a drip-tape or soaker-hose.  Also to prevent spread, DO NOT handle plants when they are wet (e.g., from dew) and routinely sterilize tools with either 10percent bleach solution or (better) 70percent alcohol (e.g., rubbing alcohol).  Where bacterial spot has been a recurring problem, consider using preventative applications of copper-based products registered for use on tomato, especially during warm, wet periods.  Keep in mind however, that if used excessively or for prolonged periods, copper may no longer control the disease.  Be sure to read and follow all label instructions of the product that you select to ensure that you use it in the safest and most effective manner possible.  Burn, bury or hot compost tomato debris at the end of the season.  Wait at least one year before planting tomatoes in a given location again, and remove and burn, bury or hot compost any volunteer tomatoes that come up in your garden.",
1:"Prune or stake plants to improve air circulation and reduce fungal problems.Make sure to disinfect your pruning shears (one part bleach to 4 parts water) after each cut.Keep the soil under plants clean and free of garden debris. Add a layer of organic compost to prevent the spores from splashing back up onto vegetation.Drip irrigation and soaker hoses can be used to help keep the foliage dry.",
2:"Two products are favored by tomato growers to protect tomato plants by regulating the temperature around a tomato plant with water.  is a self-standing set of clear tubes that surround a tomato plant. Tubes are filled with water, which warms during the day in the sunlight. Heat radiates at night to keep plants warm. has been effective in temperatures that dip down as low as 16 F.Red Tomato Teepees operate on the same principle as Wall-O-Water, the but their tubes are colored red, allowing water to heat more quickly.  Both are reusable in spring and fall and from year to year.",
3:"Plant resistant cultivars when available.Remove volunteers from the garden prior to planting and space plants far enough apart to allow for plenty of air circulation.Water in the early morning hours, or use soaker hoses, to give plants time to dry out during the day  avoid overhead irrigation.Destroy all tomato and potato debris after harvest see Fall Garden Cleanup",
4:"Upon noticing the infected areas, the first step is to let the plants air out and dry. If they are being cultivated in a greenhouse, expose them to dry air conditions, because the humidity that the fungus needs to survive and thrive is dried up in the open air.If the tomatoes are being cultivated outdoors, try to keep the leaves dry when watering the plants. One thing you can do to help keep the leaves as dry as possible is to water in the early morning hours, that way the plant has plenty of time to dry before the sun comes out, which will keep the humidity around the leaves low. You can also try drip irrigation methods, or soak watering methods to attempt to water the soil without ever wetting the leaves of the plant.Another treatment option is fungicidal sprays. When using fungicide sprays, be sure to thoroughly cover all parts of the plant that is above ground, focusing specifically on the underside of leaves. Calcium chloride sprays are among the most highly recommended types for leaf mold. There are a few organic fungicides on the market as well.",
5:"Fungicides will NOT treat this viral disease.Plant resistant varieties when available or purchase transplants from a reputable source.Do NOT save seed from infected crops.Spot treat with least-toxic, natural pest control products, such as Safer Soap, Bon-Neem and diatomaceous earth, to reduce the number of disease carrying insects.Harvest-Guard row cover will help keep insect pests off vulnerable crops/ transplants and should be installed until bloom.Remove all perennial weeds, using least-toxic herbicides, within 100 yards of your garden plot.The virus can be spread through human activity, tools and equipment. Frequently wash your hands and disinfect garden tools, stakes, ties, pots, greenhouse benches, etc. (one part bleach to 4 parts water) to reduce the risk of contamination.Avoid working in the garden during damp conditions (viruses are easily spread when plants are wet).Avoid using tobacco around susceptible plants. Cigarettes and other tobacco products may be infected and can spread the virus.Remove and destroy all infected plants (see Fall Garden Cleanup). Do NOT compost.",
6:"Septoria is caused by a fungus, Septoria lycopersici, which overwinters in old tomato debris and on wild Solanaceous plants. The fungus is spread by wind and rain, and flourishes in temperatures of 60 to 80  Controlling septoria leaf spot starts with good garden hygiene. Old plant material needs to be cleaned up, and it s best to plant tomatoes in a new location in the garden every year. One-year rotations of tomato plants have been shown to be effective in preventing the disease. Treating septoria leaf spot disease after it appears is achieved with fungicides. The chemicals need to be applied on a seven- to ten-day schedule to be effective. Spraying begins after blossom drop when the first fruits are visible. The most commonly used chemicals are maneb and chlorothalonil, but there are other options available to the home gardener. Potassium bicarbonate, ziram and copper products are a few other sprays useful against the fungus. Consult the label carefully for instructions on rate and method of application",
7:"Remove old plant debris at the end of the growing season; otherwise, the spores will travel from debris to newly planted tomatoes in the following growing season, thus beginning the disease anew. Dispose of the debris properly and don t place it on your compost pile unless you re sure your compost gets hot enough to kill the spores. Rotate crops and don t plant tomatoes in areas where other disease prone plants have been located in the past year  primarily eggplant, peppers, potatoes or, of course  tomatoes. Rutgers University Extension recommends a three-year rotation cycle to reduce soil-borne fungi. Pay careful attention to air circulation, as target spot of tomato thrives in humid conditions. Grow the plants in full sunlight. Be sure the plants aren t crowded and that each tomato has plenty of air circulation. Cage or stake tomato plants to keep the plants above the soil.",
8:"For control, use selective products whenever possible. Selective products which have worked well in the field include:bifenazate (Acramite): Group UN, a long residual nerve poisonabamectin (Agri-Mek): Group 6, derived from a soil bacteriumspirotetramat (Movento): Group 23, mainly affects immature stagesspiromesifen (Oberon 2SC): Group 23, mainly affects immature stagesOMRI-listed products include:insecticidal soap (M-Pede)neem oil (Trilogy)soybean oil (Golden Pest Spray Oil)With most miticides (excluding bifenazate), make 2 applications, approximately 5-7 days apart, to help control immature mites that were in the egg stage and protected during the first application. Alternate between products after 2 applications to help prevent or delay resistance.For current information on production methods (including varieties, spacing, seeding, and fertility), weed, disease, and insect management, please visit the New England Vegetable Management Guide.",
9:"symptomatic plants should be carefully covered by a clear or black plastic bag and tied at the stem at soil line. Cut off the plant below the bag and allow bag with plant and whiteflies to desiccate to death on the soil surface for 1-2 days prior to placing the plant in the trash. Do not cut the plant off or pull it out of the garden and toss it on the compost! The goal is to remove the plant reservoir of virus from the garden and to trap the existing virus-bearing whiteflies so they do not disperse onto other tomatoes.If symptomatic plants have no obvious whiteflies on the lower leaf surface, these plants can be cut from the garden and BURIED in the compost.Although the silverlef whitefly feeds on more than 500 plants, some of its more favorite vegetable hosts other than tomatoes include the squash and cucumber family of plants, okra, beans, peanuts & eggplant. Favorite landscape plants include hibiscus, poinsettia, Gerbera daisy and many bedding plants.Inspect plants for whitefly infestations two times per week. If whiteflies are beginning to appear, spray with azadirachtin (Neem), pyrethrin or insecticidal soap. For more effective control, it is recommended that at least two of the above insecticides be rotated at each spraying. Follow label directions closely for dosage rates, spray intervals and precautions. Spray the undersides of the leaves thoroughly."
}

strawberry_dict={0:'leaf scorch',1:'healthy strawberry'}
apple_dict={0:'Apple scab',1:'Apple black rot',2:'Apple healthy'}
tomato_dict={
0:'Tomato Bacterial spot',
1:'Tomato Early blight',
2:'tomato healthy',
3:'Tomato Late blight',
4:'Tomato Leaf mold',
5:'Tomato mosaic virus',
6:'Tomato Septoria leaf spot',
7:'Tomato Target Spot',
8:'Tomato Two spotted spider mite',
9:'Tomato Yellow leaf curl virus'
}
df = pd.read_csv("./models/treatments.csv",delimiter=";")
df.head()
df.dropna(inplace=True)

@api_view(['POST'])
def create_user_view(request):
    if request.method=="POST":
        serializer=UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            userdata = serializer.save()
            data['user']=userdata.id
            data['response']="user created ! "
        return Response(data=data,status=status.HTTP_201_CREATED)


             
@api_view(['GET'])
def user_details_view(request):
    try:
        user=User.objects.get(pk=request.GET.get('id', None))
    except User.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=UserSerializer(user)
        return Response(data=serializer.data)



@api_view(['POST'])
def update_user_view(request):
    try:
        user_toupdate = User.objects.get(pk=request.GET.get('id', None))
        if request.method == "POST":
            if request.data.get("password") is not None:
                user_toupdate.set_password(request.data.get("password"))
            if request.data.get("username") is not None :
                user_toupdate.username=request.data.get("username")
            if request.data.get("email") is not None :
                user_toupdate.email=request.data.get("email")
            user_toupdate.save()
            serialized=UserSerializer(user_toupdate)
            if serialized.is_valid:
                return Response(data=serialized.data,status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def login_user_view(request):
        user = authenticate(email=request.data.get("email"), password=request.data.get("password"))
        if user is not None : 
             serializer=UserSerializer(user)
             return Response(data=serializer.data,status=status.HTTP_200_OK)
        else :
            return Response(data={'message':'incorrect credentials'})

@api_view(['POST'])
def predictImageTomate_view(request):
    fileobj=request.FILES['imageLeaf']
    fs=FileSystemStorage()
    filepath=fs.save(fileobj.name,fileobj)
    filepathname=fs.url(filepath) 
    testimage='.'+filepathname  
    img=image.load_img(testimage,target_size=(256,256))
    img=image.img_to_array(img)
    img=img/255.0
    img_reshaped=img.reshape(1,256,256,3)
    predict=modelTomato.predict(img_reshaped)
    print(predict)
    return Response(data={'disease':tomato_dict[np.argmax(predict)],'treatment':treatment_tomato[np.argmax(predict)]},status=status.HTTP_200_OK)


@api_view(['POST'])
def predictImageApple_view(request):
    fileobj=request.FILES['imageLeaf']
    fs=FileSystemStorage()
    filepath=fs.save(fileobj.name,fileobj)
    filepathname=fs.url(filepath) 
    testimage='.'+filepathname  
    img=image.load_img(testimage,target_size=(256,256))
    img=image.img_to_array(img)
    print(img)
    img=img/255.0
    img_reshaped=img.reshape(1,256,256,3)
    predict=modelApple.predict(img_reshaped)
    print(predict)
    return Response(data={'disease':apple_dict[np.argmax(predict)],'treatment':df[apple_dict[np.argmax(predict)]]},status=status.HTTP_200_OK)


    

@api_view(['POST'])
def predictImageStrawberry_view(request):
    fileobj=request.FILES['imageLeaf']
    fs=FileSystemStorage()
    filepath=fs.save(fileobj.name,fileobj)
    filepathname=fs.url(filepath) 
    testimage='.'+filepathname  
    img=image.load_img(testimage,target_size=(256,256))
    img=image.img_to_array(img)
    img=img/255.0
    img_reshaped=img.reshape(1,256,256,3)
    predict=modelStrawberry.predict(img_reshaped)
    treatment=""
    if(strawberry_dict[np.argmax(predict)] =="leaf scorch"):
        treatment= "While leaf scorch on strawberry plants can be frustrating, there are some strategies which home gardeners may employ to help prevent its spread in the garden. The primary means of strawberry leaf scorch control should always be prevention. Since this fungal pathogen over winters on the fallen leaves of infect plants, proper garden sanitation is key. This includes the removal of infected garden debris from the strawberry patch, as well as the frequent establishment of new strawberry transplants. The creation of new plantings and strawberry patches is key to maintaining a consistent strawberry harvest, as older plants are more likely to show signs of severe infection. When making new plantings, always ensure that good planting practices are implemented. These practices include the use of proper plant spacing to provide adequate air circulation, and the use of drip irrigation. The avoidance of waterlogged soil and frequent garden cleanup will help to reduce the likelihood of spread of this fungus."
    else:
        treatment= "Nonchemical control options include selecting a well-aerated site, planting resistant or tolerant cultivars, using disease-free transplants, reducing humidity and leaf wetness by avoiding dense canopies and tight row-spacing, not over-fertilizing plants, applying overhead irrigation in the early morning to speed up drying of leaves and removing old leaf material and fruit mummies from the field at renovation. With respect to cultivar choices, it is hard to find a cultivar that is resistant to all foliar diseases, especially angular leaf spot. Or, they may be resistant to leaf spot and scorch, but not to Phomopsis leaf blight. However, the following strawberry cultivars are fairly resistant to fungal leaf spots: Allstar, Cavendish, Brunswick, Evangeline, Clancy, Guardian, Jewel, Lester, Mesabi, Ovation, Primetime, Seneca, St. Williams and Surecrop. For a list of cultivars and their disease susceptibilities, see page 213 of the 2015 Michigan Fruit Management Guide Michigan State University Extension Bulletin E0154."

    print({'disease':strawberry_dict[np.argmax(predict)],'treatment':df[strawberry_dict[np.argmax(predict)]]})
    return Response(data={'disease':strawberry_dict[np.argmax(predict)],'treatment':treatment},status=status.HTTP_200_OK)
   