const {Client} = require("pg")

require("dotenv").config()

class Database {
    
    dbConnection

    constructor(){
        this.dbConnection = new Client({
            host: process.env.db_host,
            port: process.env.db_port,
            database:  process.env.db_name,
            user: process.env.db_user,
            password: process.env.db_password,
          })
    }

    async connect() {
        this.dbConnection.connect()
    }

    async sayHello() {
        return (await this.dbConnection.query('SELECT NOW()')).rows
    }

    async useScript() {
        await this.dbConnection.query("\i /home/pachv/Code/Glawe/server/Database/db.sql")
    }
}

module.exports = new Database()