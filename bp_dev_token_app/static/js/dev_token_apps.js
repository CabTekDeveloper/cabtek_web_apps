/*------------------------------------------------------------------------------------------------------------------------*/
// Added by     : Wangchuk, 21-05-2025
// BluePrint    : bp_dev_token_app  
// File         : dev_token_apps.js
/*------------------------------------------------------------------------------------------------------------------------*/

let devTokenAppDiv = document.getElementById("dev_token_app_div");

/*------------------------------------------------------------------------------------------------------------------------*/
// Shift devTokenAppDiv to different positions randomly to prevent Screen Burn ins.
setInterval(() => {
    GlobalHelper.moveElementToDifferentPosition(devTokenAppDiv);
}, 1000 * 60 * 10); //Run every X mins 

/*------------------------------------------------------------------------------------------------------------------------*/

window.onload = async () => {
    if (window.location.pathname.includes(LocalVariables.pageName_dev_token_apps)) {
        LocalVariables.appsInDev = await DevTokenAppAPI.getAppsInDevFromDB();
    }
}


async function removeDeveloper(removeDeveloperBtn) {
    let appAndDeveloperInfoDiv = GlobalHelper.findParentElementUsingId(removeDeveloperBtn, "app_and_developer_info_div_");

    let appInfoDiv = appAndDeveloperInfoDiv.querySelector(".app_info_div")
    var app_id = appInfoDiv.dataset.app_id
    var app_name = appInfoDiv.dataset.app_name

    let developerInfoDiv = appAndDeveloperInfoDiv.querySelector(".developer_info_div")
    var developer_id = developerInfoDiv.dataset.developer_id;
    var developer_name = developerInfoDiv.dataset.developer_name;

    // Get password
    let password = prompt(`Remove '${developer_name}' from the app '${app_name}'?\n\nEnter password:`)

    if (password != null && !GlobalHelper.isEmpty(password.trim())) {
        // Validate user
        let data_to_post = {
            "user_id": developer_id,
            "password": password
        }

        let response = await GlobalAPI.validateUserInDB(data_to_post)

        if (response && response['validated']) {
            // Remove developer name from app
            data_to_post = {
                "app_id": app_id,
                "user_id": developer_id
            }
            response = await DevTokenAppAPI.removeAppInDevByFromDB(data_to_post);

            (response && response['removed']) ? GlobalHelper.redirectToURL(LocalVariables.route_bp_dev_token_app) : alert("Something went wrong!")
        }
        else {
            alert("Wrong password!");
        }
    }

}

// If the  "tbl_apps_in_dev" table data has been updated or changed in the database, then update the dev_token_apps.html.
setInterval(() => {
    if (window.location.pathname.includes(LocalVariables.pageName_dev_token_apps)) {
        checkAppsInDevChangesInDB();
    }
}, 1000)

async function checkAppsInDevChangesInDB() {
    let oldData = LocalVariables.appsInDev
    let newData = await DevTokenAppAPI.getAppsInDevFromDB()

    let oldData_stringfy = JSON.stringify(oldData);
    let newData_stringyfy= JSON.stringify(newData);

    var dataUpdatedInDB = oldData_stringfy != newData_stringyfy
    
    if (dataUpdatedInDB){
        LocalVariables.appsInDev = newData;
        GlobalHelper.redirectToURL(LocalVariables.route_bp_dev_token_app);
    }

}


/*------------------------------------------------------------------------------------------------------------------------*/






