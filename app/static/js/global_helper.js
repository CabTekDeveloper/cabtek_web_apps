/*------------------------------------------------------------------------------------------------------------------------*/
// Added by     : Wangchuk, 21-05-2025
// BluePrint    : app  
// File         : global_helper.js

/*------------------------------------------------------------------------------------------------------------------------*/
// Static Class: Global Helper functions

class GlobalHelper {
    constructor() {
        if (this instanceof GlobalHelper) {
            throw Error("A static class cannot be instantiated.") // Contructor : Stop users from creating instances of this class
        }
    }

    static redirectToURL(url) {
        window.location.href = (url)
    }

    static closeModal(modalId) {
        document.getElementById(modalId).style.display = "none";
    }

    static openModal(modalId) {
        document.getElementById(modalId).style.display = "block";
    }

    static hideElement(element) {
        if (!element.classList.contains("hide")) element.classList.add("hide");
    }

    static unHideElement(element) {
        if (element.classList.contains("hide")) element.classList.remove("hide");
    }

    static addClass(element, className) {
        element.classList.add(className);
    }

    static removeClass(element, className) {
        element.classList.remove(className);
    }

    static isEmpty(value) {
        return (
            value === null ||
            value === undefined ||
            value === '' ||
            (Array.isArray(value) && value.length === 0) ||
            (typeof value === 'object' && Object.keys(value).length === 0)    // Checks for empty object
        );
    }

    // Generate random number and round to 2 decimal palces
    static generateRandomNumber(min, max) {
        let randNum = Math.random() * (max - min + 1) + min
        return randNum.toFixed(2);
    }

    static isAlphaNumeric(text) {
        return /^[a-zA-Z0-9]*$/.test(text);
    }

    static deepCopyObject(obj) {
        return JSON.parse(JSON.stringify(obj));
    }

    static getWindowWidth() {
        return window.innerWidth;
    }

    static getWindowHeight() {
        return window.innerHeight;
    }

    static getElementWidth(element) {
        const rect = element.getBoundingClientRect();
        return rect.right - rect.left;
    }

    static getElementHeight(element) {
        return element.clientHeight;
    }

    // This function will generate a new random left offset so that the right boundary of the elment barely touches the right of the window
    static generateRandomLeftOffsetForHtmlElement(element) {
        let elWidth = this.getElementWidth(element);
        let wWidth = this.getWindowWidth();
        let max = Math.abs(wWidth - elWidth);
        return this.generateRandomNumber(0, max);
    }

    // This function will generate a new random top offset so that the bottom boundary of the elment barely touches the bottom of the window
    static generateRandomTopOffsetForHtmlElement(element) {
        let elHeight = this.getElementHeight(element);
        let wHeight = this.getWindowHeight();
        let max = Math.abs(wHeight - elHeight);
        return this.generateRandomNumber(0, max);
    }

    //  Move Html Element to a new position
    static moveElementToDifferentPosition(elementToMove) {
        // Generate random Left and Top Offsets
        const newLeft = this.generateRandomLeftOffsetForHtmlElement(elementToMove)
        const newTop = this.generateRandomTopOffsetForHtmlElement(elementToMove)
        // Set the new positions
        elementToMove.style.left = newLeft + "px";
        elementToMove.style.top = newTop + "px";
    }

    // To find parent element of the current elment using only partial or full parent id
    static findParentElementUsingId(childElement, parentId) {
        let parentElement = childElement.closest(`[id*='${parentId}']`)
        return parentElement;
    }

    static findParentElementUsingClass(childElement, parentClass) {
        let parentElement = childElement.closest(`[class*='${parentClass}']`)
        return parentElement;
    }

    static buildHtmlForSelectOptionTag(value, innerHtml) {
        return `<option value="${value}">${innerHtml}</option>`;

    }
}



// Add all of the functions below to the class above.


















// function filterOutSectionNames(AllSectionNames, filter) {
//     let filteredSectionNames = [];
//     filteredSectionNames = AllSectionNames.filter(item => !filter.includes(item['section_name']));
//     return filteredSectionNames;
// }



// function buildHTMLforSectionNameBtn(sectionName) {
//     return `<a href="#" onclick="sectionNameOnClick(this)" type="button" class="btn btn-sm d-inline-block bold">${sectionName}</a>`
// }





