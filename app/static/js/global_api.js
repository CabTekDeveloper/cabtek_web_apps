/*------------------------------------------------------------------------------------------------------------------------*/
// Added by     : Wangchuk, 21-05-2025
// BluePrint    : app  
// File         : global_api.js

/*------------------------------------------------------------------------------------------------------------------------*/
// Static Class: Global Api call functions

class GlobalAPI {
    // Static variables
    static URL_PREFIX = "";

    static OPTIONS_GET = { method: "GET" };

    static OPTIONS_POST_JSON_DATA = {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: null
    }

    static OPTIONS_POST_FORM_DATA = {
        method: "POST",
        body: null
    }


    // Contructor : Stop users from creating instances of this class
    constructor() {
        if (this instanceof GlobalAPI) {
            throw Error("A static class cannot be instantiated.")
        }
    }

    // GET methods
    static async getSingleUserByUserIdFromDB(user_id) {
        let data = [];
        const url = `${this.URL_PREFIX}/get_single_user_by_id_db/${user_id}`;
        const res = await fetch(url, this.OPTIONS_GET);
        if (res.status == 200) { data = await res.json(); }
        return data;
    }

    // Post methods
    static async validateUserInDB(data_to_post) {
        this.OPTIONS_POST_JSON_DATA.body = JSON.stringify(data_to_post);
        let data = {}
        const url = `${this.URL_PREFIX}/user_validation`;
        const res = await fetch(url, this.OPTIONS_POST_JSON_DATA);
        if (res.status == 200) { data = await res.json(); }
        return data;
    }
}
