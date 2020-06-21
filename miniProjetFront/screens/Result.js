import React,{useState,useEffect} from 'react';
import { View, Text, StyleSheet, ScrollView ,Image} from 'react-native';
import { Title } from 'react-native-paper';



export  default function Result ({navigation,route})
{

    const [disease,setDisease] = useState({disease:'',treatment:''});
    useEffect(()=>{
        setDisease({disease:route.params.disease,treatment:route.params.treatment})
    },[])
   
   
   
    return (
        <View style={styles.container}>
        <View style={styles.header}>
            <Title style={styles.Title}>{disease.disease} </Title>
        </View>
        <ScrollView>
            <View style={styles.body}>
                <View style={styles.aboutText}>
                    <Text style={styles.text}>
                     </Text>
                </View>
                <View>
                    <Title style={styles.Title}>Treatment</Title>

                </View>
                <View style={styles.aboutText}>
                    <Text style={styles.text}>
                        {disease.treatment}
                     </Text>
                </View>
            </View>


        </ScrollView >

    </View >
)
}



const styles = StyleSheet.create({
teamMember:{
    fontSize:20, 
    letterSpacing: 1,
    fontWeight: '100',
    textAlign: 'center',
    marginVertical: 10
},
profilePicture: {
    marginVertical:10,
    width: 100,
    height: 100,
    borderRadius: 200
},
text: {
    letterSpacing: 2,
    textAlign: 'center',
},
container: {
    flex: 1,
    backgroundColor: 'white',

},
header: {
    marginTop: 15,
    marginLeft: 10,
    width: '100%',
    height: 70,
},
Title: {
    fontSize: 30,
    letterSpacing: 1,
    fontWeight: '100',
    textAlign: 'center',
    marginVertical: 10,
    color:'#00a32b'
},
body: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    width: "100%",


},
aboutText: {
    marginHorizontal: 9,
    width:"80%",
    borderBottomColor:'grey',
    marginBottom:15,
    borderBottomWidth:1,
    paddingVertical:5
}
})

       
       
    

