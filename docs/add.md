

<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/7.22.0/firebase-app.js"></script>


<script src="https://www.gstatic.com/firebasejs/7.22.0/firebase-auth.js"></script>


<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="https://www.gstatic.com/firebasejs/7.22.0/firebase-analytics.js"></script>

<script>
  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyBoHkYnORpBCQJrqR8GzDtW4Iz_6GJpHuQ",
    authDomain: "apollo-bb64b.firebaseapp.com",
    databaseURL: "https://apollo-bb64b.firebaseio.com",
    projectId: "apollo-bb64b",
    storageBucket: "apollo-bb64b.appspot.com",
    messagingSenderId: "544817195656",
    appId: "1:544817195656:web:735acb42a3cfcbee6a0d3d",
    measurementId: "G-HFZHHRFKJ9"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();

  const auth = firebase.auth();

  function singUp(){
      var email = document.getElementById("txtEmail");
      var password = document.getElementById("txtPassword");

      const promise = auth.createUserWithEmailAndPassword(email.value,password.value);
      promise.catch(e => alert(e.message));

      alert("Signed UP");
  }


  function Login(){
      var email    = document.getElementById("txtEmail");
      var password = document.getElementById("txtPassword");

      const promise = auth.signInWithEmailAndPassword(email.value,password.value);
      promise.catch(e => alert(e.message));

      alert("Logged In as: " + email.value);

  }

  auth.onAuthStateChanged(function(user){
      if(user){
      document.getElementById("Form").innerHTML = 5 + 6;

      }else{
          alert("No active User")
          document.getElementById("Form").innerHTML = "HI";

      }
  });
</script>

<div> 

<input  id="txtEmail"    type="email"     placeholder="Email"  style="border-style: outset;">
<input  id="txtPassword" type="password"  placeholder="Password">

<button onclick="Login()" id="btnLogin"    style="background-color: #4CAF50;border: none;color: white;padding: 15px 32px;text-align: center;display: inline-block font-size: 16px;"> Log in  </button>

<button onclick="singUp()" id="btnLogin"    style="
 background-color: #401F9F;border: none;color: white;padding: 15px 32px;text-align: center;display: inline-block font-size: 16px;"> Sing Up </button>
<p id="Form"> Hi </p>

</div>


<div>
<label for="tutorialtitle">Tutorial Title</label>
</div>
<div>


<textarea id="tutorialtitle" name="tutorialtitle" rows="1" cols="100">
Add your Title Here!
</textarea>
</div>


<div>
<label for="tutorialtext">Tutorial Text</label>
</div>
<div>


<textarea id="tutorialtext" name="tutorialtext" rows="20" cols="100">
Add your tutorial here!
</textarea>
</div>
