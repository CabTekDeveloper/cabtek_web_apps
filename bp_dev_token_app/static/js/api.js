/*------------------------------------------------------------------------------------------------------------------------*/
// Added by     : Wangchuk, 21-05-2025
// BluePrint    : bp_dev_token_app  
// File         : api.js

/*------------------------------------------------------------------------------------------------------------------------*/
// Static Class: Dev Token App Api call functions
/*------------------------------------------------------------------------------------------------------------------------*/
class DevTokenAppAPI {
    // Static variables
    static URL_PREFIX = "/bp_dev_token_app";

    static OPTIONS_GET = { method: "GET" };

    static OPTIONS_POST_JSON_DATA = {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: null
    };

    static OPTIONS_POST_FORM_DATA = {
        method: "POST",
        body: null
    };

    // Contructor : Stop users from creating instances of this class
    constructor() {
        if (this instanceof DevTokenAppAPI) {
            throw Error("A static class cannot be instantiated.")
        }
    }

    // GET methods
    static async getDeveloperListFromDB() {
        const url = `${this.URL_PREFIX}/get_developer_list_from_db`;
        let data = []
        const res = await fetch(url, this.OPTIONS_GET);
        if (res.status == 200) { data = await res.json(); }
        return data
    }

    static async getAppsInDevFromDB() {
        const url = `${this.URL_PREFIX}/get_apps_in_dev_db`;
        let data = []
        const res = await fetch(url, this.OPTIONS_GET);
        if (res.status == 200) { data = await res.json(); }
        return data
    }


    // POST Methods : JSON DATA
    static async assignDeveloperToAppInDB(data_to_post) {
        this.OPTIONS_POST_JSON_DATA.body = JSON.stringify(data_to_post);
        let data = {}
        const url = `${this.URL_PREFIX}/assign_developer_to_app_db`;
        const res = await fetch(url, this.OPTIONS_POST_JSON_DATA);
        if (res.status == 200) { data = await res.json(); }
        return data;
    }

    static async removeAppInDevByFromDB(data_to_post) {
        this.OPTIONS_POST_JSON_DATA.body = JSON.stringify(data_to_post);
        let data = {}
        const url = `${this.URL_PREFIX}/remove_app_in_dev_by_db`;
        const res = await fetch(url, this.OPTIONS_POST_JSON_DATA);
        if (res.status == 200) { data = await res.json(); }
        return data;
    }

    // POST Methods : FORM DATA
    // async function xxxxxxxxxx(uploadedFile, user_id) {
    //     let data = {}
    //     const formData = new FormData()
    //     formData.append("uploadedFile", uploadedFile)
    //     formData.append("user_id", user_id)
    //     const url = `/save_eo_excel_file_text_to_db`;
    //     OPTIONS_POST_FORM_DATA.body = formData;
    //     const res = await fetch(url, OPTIONS_POST_FORM_DATA);
    //     if (res.status == 200) { data = await res.json(); }
    //     return data;
    // }

}





