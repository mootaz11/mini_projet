import React from 'react';
import { View, StyleSheet, TouchableOpacity, Text } from 'react-native';
import { AuthContext } from '../navigation/context';
import FlatButton from '../common/FlatButton';
import Field from '../common/Field';
import { Title } from 'react-native-paper'
import { Formik } from 'formik';
import * as yup from 'yup';
import {register} from '../api/rest';

const Fields = [
{ placeholder: 'username' , name:'username',type:'username',secureTextEntry:false},
{ placeholder: 'email',name:'email' ,type:'username',secureTextEntry:false}, 
{ placeholder: 'password',name:'password',type:'password',secureTextEntry:true},
{ placeholder: 'confirm password',name:'password1',type:'password',secureTextEntry:true}

];

export default function Signup({ navigation }) {
    var isSignedUp = false ;
    const RegisterSchema = yup.object({
        username:yup.string().required('username is required').min(6,'username length is short'), 
        email:yup.string().email('email is invalid .').required('email is required .'),
        password:yup.string().min(6,'password is weak').required('password is required .'),
        password1:yup.string().oneOf([yup.ref('password')],'password not match')
    })
    
    const signup = (values) =>{
        register(values,(res)=>{
            if(res.status==201)
            {
                navigation.navigate("Login")
                console.log(res.data);

            }    
            else {
                console.log("something's wrong")
            }
        })
        
        isSignedUp=true;
        setTimeout(() => {
            isSignedUp=false;
        }, 1000);
    }
    return (
        <View style={styles.container}>
            <View style={styles.Header}>
                <Title style={styles.title}>Signup</Title>
            </View>
            <Formik
                initialValues={{ username: '', email: '', password: '', password1: '' }}
                validationSchema={RegisterSchema}
                onSubmit={(values,actions) => {
                        signup(values);
                        actions.resetForm();
                }}
                >
                {
                    (props) =>
                     (
                         <React.Fragment>
                        <View style={styles.form}>
                            {Fields.map((value, i) => {
                                return (
                                    <Field
                                        placeholder={value.placeholder}
                                        onChange={props.setFieldValue}
                                        onTouch={props.setFieldTouched}
                                        name={value.name}
                                        value={props.values[value.name]}
                                        error={props.touched[value.name] && props.errors[value.name]}
                                        secureTextEntry={value.secureTextEntry}
                                        key={i}
                                    />
                                )
                            })}
                        </View>
                         <View style={styles.LoginContainer}>
                            <TouchableOpacity onPress={props.handleSubmit}>
                                <FlatButton
                                    text="Sign up"
                                />
                            </TouchableOpacity>
                           
                            {
                                isSignedUp ? 
                                (
                                    <Text style={styles.sign}>you signed up successfully !</Text>

                                ):( 
                                      <Text style={styles.sign}></Text>
                                    )
                            }
                        
                        </View>
            </React.Fragment>
                )
            }
            </Formik>


        </View>
    )

}


const styles = StyleSheet.create({

    container: {
        flexDirection: 'column',
        backgroundColor: 'white',
        width: "100%",
        height: "100%"

    },
    Header: {
        marginBottom: 10,
        marginLeft:15
    },
    title: {
        fontSize: 30,
        marginTop: 15
    },
    form: {
        flex: 1,
        alignItems: 'center',
        marginBottom: 120

    },

    LoginContainer: {
        marginTop: 35,
        flex: 1,
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center'
    },

    sign:{
        color:'grey',
        marginTop:5,
        justifyContent:'center',
        alignItems:'center'
    }


})
