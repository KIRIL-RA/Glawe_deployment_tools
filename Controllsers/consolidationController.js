
class ConsolidationController {
    async getFormattedMetrics(req,res,next) {
        try {

            console.log("works here");
            return res.status(200).json({
                metrics : [
                    {
                        name: "csd",
                        type: "best_type",
                        units_of_measurement : "ml",
                        value: 123,
                        time_start: new Date(),
                        time_end: new Date()
                    },
                    {
                        name: "ok",
                        type: "best_type",
                        units_of_measurement : "ml",
                        value: 123,
                        time_start: new Date(),
                        time_end: new Date()
                    }
                ]

        })
        } catch (error) {
            console.log(error);
        }
    }

    async getAvailableMetrics(req,res,next) {
        try {
            return res.status(200).json({
                page: 12,
                hasNext:true,
                hasPrev:true,
                sources:[
                    {
                        source_name: "machine",
                        types: "graph",
                        data : [
                            {
                                machine_name: "machine-001",
                                machine_type: "type--2",
                                machine_tablet_id: "table-32442",
                                shop_id: "sf23r",
                                machine_state: "active"

                            },
                            {
                                machine_name: "machine-021",
                                machine_type: "type--2",
                                machine_tablet_id: "table-32442",
                                shop_id: "sf23r",
                                machine_state: "active"

                            },
                        ]
                    },
                    {
                        source_name: "worker",
                        types: "graph",
                        data : [
                            {
                                fullName: "Dima Dimitry Demitrovich",
                                phoneNumber: "88005553434",
                                on_work_place: true,
                                position: "worker",
                                metrics: [
                                    {
                                        name: "oee",
                                        type: "cool type",
                                        units_of_measurement: "big units",
                                        value: "big value",
                                        time_start: new Date(),
                                        time_end: new Date()
                                    },
                                    {
                                        name: 'kpe',
                                        type: "cool type",
                                        units_of_measurement: "big units",
                                        value: "big value",
                                        time_start: new Date(),
                                        time_end: new Date()
                                    },
                                ]
                            }
                        ],

                    },
                ]
        })
        } catch (error) {
            console.log(error);
        }
    }
}

module.exports = new ConsolidationController()