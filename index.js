const express = require("express")
const cors = require('cors')

const mainRouter = require("./routers/mainRouter")

const db = require("./Database/db")

// setting up config
require("dotenv").config()

const app = express()

app.use(cors())
app.use(express.json())
app.use("/api/v1",mainRouter)

const runApp = async () => {
    try {
        await db.connect()
        app.listen(process.env.server_port,()=>{
            console.log(`server is started on port ${process.env.server_port}`);
        })
    } catch (e) {
        console.log(e);
    }
}

runApp()