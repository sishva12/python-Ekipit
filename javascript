<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datatypes,variables,operators</title>
    <script>
        // using  variables var ,let,const key words
        function add(a,b){
            var a;
            var b;
            result= a+b;
            console.log(" after adding result is "+result)
        }
        function sub(a,b){
            var a;
            var b;
            result= a-b;
            console.log("after substracting result is "+result)
        }
        function mult(b){
            const a=45;
            var b;
            result= a*b;
            console.log("after multiplying result is "+result)
        }
        function div(a,b){
            let x;
            let y;
            result= a/b;
            console.log("after dividing result is "+result)
        }
        add(22,77);
        sub(20,30);
        mult(22);
        div(345,7);
//data types 
      s=25
        i=45000.00
        t=56.89
        e=1234567890
        j=true
        p='l'
        m="string data type"
        console.log(typeof s)
        console.log(typeof i)
        console.log(typeof p)
        console.log(typeof e)
        console.log(typeof j)
        console.log(typeof m)
//conditional statements
        k=10
        if(k!=0){
            console.log("false")
        }else if(k===10){
            console.log("true")
        }else{
            console.log("pi vevi kavu")
        }

//for loop
    var clothes = ["t-shirts","jeans","baneen","pant","shot"];
for(var i =0; i<=clothes.length; i++){
    document.write(clothes[i]+",")
}

    </script>
 
</head>
<body>
</body>
</html>
