import React, { useState,useEffect } from 'react';
import { View, TouchableOpacity, StyleSheet, Image } from 'react-native';
import { Title } from 'react-native-paper';
import FlatButton from '../common/FlatButton';
import { ActionSheet, Root } from 'native-base';
import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';
import {checkDisease,checkDiseaseTomato,checkDiseaseStrawberry} from '../api/rest'

export default function Action({ navigation, route }) {

    const [image, setImage] = useState(" ");
    const [disease,setDisease]=useState("");
    console.log(route.params.ServiceName);
    console.log(disease.disease);
    useEffect(()=>{
        setImage(" "),
        setDisease("");
    },[])
    const OnclickcheckDisease = ()=>{
        if(disease != ''){
            navigation.navigate("Result",{disease:disease.disease,treatment:disease.treatment});
        }    
         
            }

    const chooseFromCamera=async ()=>{
        await Permissions.askAsync(Permissions.CAMERA);
        await Permissions.askAsync(Permissions.CAMERA_ROLL);
        let result=await ImagePicker.launchCameraAsync({
            allowsEditing: true,
            base64: true
      
        })
        console.log(result.uri);
        const formdata= new FormData();

        formdata.append('imageLeaf',{type:'image/png',uri:result.uri,name:'upload.png'});    

        
        if(    route.params.ServiceName =="Apple Service")
        {
          checkDisease(formdata,(res)=>{
              console.log(res);
              setDisease(res.data);
        });
        } 
        if(    route.params.ServiceName =="Tomato Service")
        { 

          checkDiseaseTomato(formdata,(res)=>{
              setDisease(res.data);
              console.log(res.data);

          })
        } 
        if(    route.params.ServiceName =="Strawberry Service")
        {
          checkDiseaseStrawberry(formdata,(res)=>{
              console.log(res.data);
              setDisease(res.data);
        });
        } 
    
        if (!result.cancelled) {
          setImage(result.uri);
        }

    }
    const chooseFromLibrary=async ()=>{


        let result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.Images,
            allowsEditing: true,
            aspect: [4, 3],
            quality: 1,
          });
      
          const formdata= new FormData();
          formdata.append('imageLeaf',{type:'image/png',uri:result.uri,name:'upload.png'});   


          if(    route.params.ServiceName =="Apple Service")
          {
            checkDisease(formdata,(res)=>{
                console.log(res);
                setDisease(res.data);
          });
          } 
          if(    route.params.ServiceName =="Tomato Service")
          { 

            checkDiseaseTomato(formdata,(res)=>{
                setDisease(res.data);
                console.log(res.data);

            })
          } 
          if(    route.params.ServiceName =="Strawberry Service")
          {
            checkDiseaseStrawberry(formdata,(res)=>{
                console.log(res.data);
                setDisease(res.data);
          });
          } 
      

        if (!result.cancelled) {
            setImage(result.uri);
          }
    }
    const addImage = () => {
        const BUTTONS = ['Take a photo', 'Choose from Library', 'Cancel'];
        ActionSheet.show(
            { options:BUTTONS, cancelButtonIndex: 2, title: 'Select a photo'}, (index) => {
                switch (index) {
                    case 0:
                        chooseFromCamera();
                        break;
                    case 1:
                        chooseFromLibrary();
                        break;
                    default:
                        break;
                }
            })
    }

    return (
        <Root>
            <View style={styles.container}>
                <View style={styles.Header}>
                    <Title style={styles.title}>disease classification</Title>
                </View>
                <View style={styles.imageContainer}>
                    <Image style={styles.image} source={{uri:image}} />
                </View>

                <View >
                    <TouchableOpacity onPress={addImage}>
                        <FlatButton 
                            text="Choose Leaf image" />
                    </TouchableOpacity>
                    <TouchableOpacity onPress={OnclickcheckDisease}>
                        <FlatButton 
                            text="Check Disease" />
                    </TouchableOpacity>


                </View>

            </View>
        </Root>


    );
}
const styles = StyleSheet.create({

    container: {
        flex: 1,
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'white',
        width: "100%",
        height: "100%"

    },
    Header: {
        margin: 10
    },
    title: {
        fontSize: 30,
        marginTop: 5
    },
    image: {
        width: 100,
        height: 180,
    },
    imageContainer: {
        padding: 50,
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center'
    }


})

