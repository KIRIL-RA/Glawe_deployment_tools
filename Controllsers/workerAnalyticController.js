class WorkerAnalyticController {
    async getWorkerMetrics(req,res,next) {
        try {
            return res.status(200).json({
                fullName: "Dima Dimitry Demitrovich",
                phoneNumber: "88005553434",
                on_work_place: true,
                position: "worker",
                metrics : [
                    {
                        name: "oee",
                        type: "cool type",
                        units_of_measurement : "big units",
                        value : "big value",
                        time_start: new Date(),
                        time_end: new Date()
                    },
                    {
                        name: 'kpe',
                        type: "cool type",
                        units_of_measurement : "big units",
                        value : "big value",
                        time_start: new Date(),
                        time_end: new Date()
                    },
                ]

        })
        } catch (error) {
            console.log(error);
        }
    }
}

module.exports = new WorkerAnalyticController()