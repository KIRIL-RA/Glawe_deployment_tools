
class AlertsController {
    async getUnreadedAlerts(req,res,next) {
        try {
            return res.status(200).json({
                alerts: [
                    {
                        message:"hi",
                        action_name: "help",
                        action_type: "type",
                        action_status: "sfsf",
                        action_time: new Date()
                    },
                    {
                        message:"hi",
                        action_name: "help",
                        action_type: "type",
                        action_status: "sfsf",
                        action_time: new Date()
                    },

                ]
            })
        } catch (error) {
            console.log(error);
        }
    }

    async closeAlert(req,res,next) {
        try {
            return res.status(200).json({
                status: "ok"
            })
        } catch (error) {
            console.log(error);
        }
    }

    async getOutdatedMessages(req,res,next) {
        try {
            return res.status(200).json({
                page:0,
                hasNext:true,
                hasPrev:true,
                alerts: [
                    {
                        message:"ok",
                        action_name:"type",
                        action_type:"good type",
                        action_status: " ok",
                        action_time: new Date()
                    },
                    {
                        message:"not ok",
                        action_name:"type",
                        action_type:"good type",
                        action_status: " ok",
                        action_time: new Date()
                    },
                ]


            })
        } catch (error) {
            console.log(error);
        }
    }
}

module.exports = new AlertsController()