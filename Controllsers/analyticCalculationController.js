
class AnalyticCalculationController {
    async getMachineState(req,res,next) {
        try {
            res.status(200).json({
                machine_name: "machine-001",  
                machine_type: "type--2",
                machine_tablet_id: "table-32442",  
                shop_id: "sf23r",
                machine_state: "active"
  
            })
        } catch (error) {
            console.log(error);
        }
    }

    async getMachinesFromShop(req,res,next) {
        try {
            res.status(200).json({
                shop_name:"wonder shop",
                manufacture_id:  "2389d98j" ,
                page: "0",
                has_next: true,
                has_prev: true,
                machines: [
                    {
                        machine_name: "machine-001",  
                        machine_type: "type--2",
                        machine_tablet_id: "table-32442",  
                        shop_id: "sf23r",
                        machine_state: "active" 
                    },
                    {
                        machine_name: "machine-001",  
                        machine_type: "type--2",
                        machine_tablet_id: "table-32442",  
                        shop_id: "sf23r",
                        machine_state: "active" 
                    },
                    {
                        machine_name: "machine-001",  
                        machine_type: "type--2",
                        machine_tablet_id: "table-32442",  
                        shop_id: "sf23r",
                        machine_state: "active" 
                    },
                ] 
  
            })
        } catch (error) {
            console.log(error);
        }
    }

    
    async getMachinesFromManifacture(req,res,next) {
        try {
            return res.status(200).json({
                shop_name:"super shop",
                manufacture_id:  "ab7828c78syd" ,
                manufacture_name: "super manufacture",
                page: 0,
                has_next: true,
                has_prev: true,
                machines: [
                    {
                        machine_name: "machine-001",  
                        machine_type: "type--2",
                        machine_tablet_id: "table-32442",  
                        shop_id: "sf23r",
                        machine_state: "active" 
                    },
                    {
                        machine_name: "machine-001",  
                        machine_type: "type--2",
                        machine_tablet_id: "table-32442",  
                        shop_id: "sf23r",
                        machine_state: "active" 
                    },
                    {
                        machine_name: "machine-001",  
                        machine_type: "type--2",
                        machine_tablet_id: "table-32442",  
                        shop_id: "sf23r",
                        machine_state: "active" 
                    },
                ] 
  
            })
        } catch (error) {
            console.log(error);
        }
    }


}

module.exports = new AnalyticCalculationController()