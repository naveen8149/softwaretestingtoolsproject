
 // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyBlbH42JJrx1LIWS4fYQh7tLQibiLDBpN8",
    authDomain: "eshop-724dc.firebaseapp.com",
    databaseURL: "https://eshop-724dc.firebaseio.com",
    projectId: "eshop-724dc",
    storageBucket: "eshop-724dc.appspot.com",
    messagingSenderId: "160815007701",
    appId: "1:160815007701:web:290257a36b8671a7b8df5c"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  const auth = firebase.auth();
  var valid=false;

  function Register(){
    var email = document.getElementById("inputEmail").value;
    var password = document.getElementById("inputPassword").value;
    if(valid==true){

    const promise = auth.createUserWithEmailAndPassword(email,password);
    promise.catch(e => alert(e.message));

    alert("User SignedUp");
    document.getElementById('myForm').submit();
    

  }
  else{
    alert("password does not match");
    document.getElementById("myForm").reset();

  }
  
  }

function check(){
         var pass  = document.getElementById("inputPassword").value;
         var rpass  = document.getElementById("inputConfirmPassword").value;
        if(pass != rpass){
            valid=false;
            
        }else{
            valid = true;
        }
}

function login(){
  var email = document.getElementById("inputEmail").value;
    var password = document.getElementById("inputPassword").value;

    const promise = auth.signInWithEmailAndPassword(email,password);
    promise.catch(e => alert(e.message));

    alert("Login successfull");

}