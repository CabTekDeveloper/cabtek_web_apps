/*------------------------------------------------------------------------------------------------------------------------*/
// Added by     : Wangchuk, 12-06-2025
// BluePrint    : bp_dev_token_app  
// File         : local_variables.js
// Purpose      : Store all the variables of current Bluprint JS modules
/*------------------------------------------------------------------------------------------------------------------------*/

class LocalVariables {

    // Contructor : Stop users from creating instances of this class
    constructor() {
        if (this instanceof BpVariables) {
            throw Error("A static class cannot be instantiated.")
        }
    }

    static appsInDev = [];

    static pageName_dev_token_apps = "dev_token_apps";

    static route_bp_dev_token_app = "/bp_dev_token_app"

    
}