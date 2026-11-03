const express == require('express')
const app = express();
app.use(express.json());
let products = [
    {id:1,name:'laptop',price:7500},
    {id:2,name:'Mouse' ,price:5000},
    {id:3,name:'keyboard',price:1200}
   ];
let nextd=4;
app.get('/product',(req,res)=>{
    res.json(products);
    });
app.post('/product',(req,res)=>{
    const product = {
        id:nextid++,
        name:req.body.name,
        price:req.body.price
        };
    products.push(product);
    res.status(201).json(product);
    });
app.listen(3000,()=>{
    console.log('server running on port 3000');
    });
