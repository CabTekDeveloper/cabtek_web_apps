/*------------------------------------------------------------------------------------------------------------------------*/
// Added by     : Wangchuk, 21-05-2025
// BluePrint    : bp_dev_token_app  
// File         : modal_assign_developer.js
/*------------------------------------------------------------------------------------------------------------------------*/
let modalAssignDeveloper = document.getElementById("modal_assign_developer");
let headerModalAssignDeveloper = modalAssignDeveloper.querySelector("#modal_header");
let closemodalAssignDeveloper = modalAssignDeveloper.querySelector("#close_modal_btn");
let developerSelectTag = modalAssignDeveloper.querySelector("#select_tag");
let commitButton = modalAssignDeveloper.querySelector("#commit_btn");

// Store the active elements in this global variable to help with HTML elment content manipulation.
// Don't foreget to reset this variable whereever necessary to prevent it from storing old data.
let GlobalVariable = {
    "appAndDeveloperInfoDiv": null,
    "appInfoDiv": null,
    "app_id": null,
    "app_name": null,
};

/*------------------------------------------------------------------------------------------------------------------------*/
// Reset Modal
function resetModalAssignDeveloper() {
    GlobalVariable = {
        "appAndDeveloperInfoDiv": null,
        "appInfoDiv": null,
        "app_id": null,
        "app_name": null,
    };
}

// Close Modal Button
if (closemodalAssignDeveloper != null) {
    closemodalAssignDeveloper.onclick = (e) => GlobalHelper.closeModal(modalAssignDeveloper.id);
}


// Load Modal
function loadModalAssignDeveloper(assignDeveloperBtn) {
    // Reset modal variables
    resetModalAssignDeveloper();
    // Find the selected App and developer info div for the clicked button
    let appAndDeveloperInfoDiv = GlobalHelper.findParentElementUsingId(assignDeveloperBtn, "app_and_developer_info_div_");
    if (appAndDeveloperInfoDiv) {
        // Set gloabl variable values
        let appInfoDiv = appAndDeveloperInfoDiv.querySelector(".app_info_div");
        GlobalVariable.appAndDeveloperInfoDiv = appAndDeveloperInfoDiv;
        GlobalVariable.appInfoDiv = appInfoDiv;
        GlobalVariable.app_id = appInfoDiv.dataset.app_id;
        GlobalVariable.app_name = appInfoDiv.dataset.app_name;

        // Open modal and set the contents
        GlobalHelper.openModal(modalAssignDeveloper.id)
        updateModalHeader();
        updateAssignDeveloperSelectTag();
    }
}

function updateModalHeader() {
    let appNameTag = `<span class="text-bold" data-app_id=${GlobalVariable.app_id}>${GlobalVariable.app_name}</span>`
    headerModalAssignDeveloper.innerHTML = `Assign developer to ${appNameTag}`;
}

async function updateAssignDeveloperSelectTag() {
    let developers = await DevTokenAppAPI.getDeveloperListFromDB();
    let options = "<option></option>"
    if (developers.length > 0) {
        for (var developer of developers) {
            options += GlobalHelper.buildHtmlForSelectOptionTag(developer.id, developer.name)
        }
    }
    developerSelectTag.innerHTML = options;
}

// Event: Select option on change
if (developerSelectTag != null) {
    developerSelectTag.onchange = (e) => {
        var optionValue = developerSelectTag.options[developerSelectTag.selectedIndex].value.trim();
        GlobalHelper.isEmpty(optionValue) ? GlobalHelper.hideElement(commitButton) : GlobalHelper.unHideElement(commitButton);
    };
}


// Event: commitButton on click
if (commitButton != null) {
    commitButton.onclick = (e) => assignDeveloperToApp();
}


// Assign selected developer to app in the database
async function assignDeveloperToApp() {
    let selectedOptionTag = developerSelectTag.options[developerSelectTag.selectedIndex];
    let developer_name = selectedOptionTag.innerText;
    let developer_id = selectedOptionTag.value.trim();

    if (!GlobalHelper.isEmpty(developer_id)) {
        let password = prompt(`Add '${developer_name}' to the app '${GlobalVariable.app_name}'?\n\nEnter password:`)
        if (password != null && !GlobalHelper.isEmpty(password.trim())) {
            // Validate User
            let data_to_post = { "user_id": developer_id, "password": password }
            let response = await GlobalAPI.validateUserInDB(data_to_post)
            
            if (response && response['validated']) {
                // Assign develover to app
                data_to_post = { "app_id": GlobalVariable.app_id, "user_id": developer_id }
                response = await DevTokenAppAPI.assignDeveloperToAppInDB(data_to_post);
                response && response['success'] ? GlobalHelper.redirectToURL(LocalVariables.route_bp_dev_token_app) : alert("Something went wrong!");
            }
            else {
                alert("Wrong password!");
            }
        }

    }

}


