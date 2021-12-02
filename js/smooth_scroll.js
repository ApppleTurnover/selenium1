const callback = arguments[arguments.length - 1]
const scroll_element = arguments[0]
const neededScroll = arguments[1]

const powerRange = arguments[2]
const sleepRange = arguments[3]
const scrollStop = 800
const timeoutWaitScroll = 50

function waitScroll() {
    let position = null
    const checkIfScrollIsStatic = setInterval(() => {
        if (position === window.scrollY) {
            clearInterval(checkIfScrollIsStatic)
            callback()
        }
        position = window.scrollY
    }, timeoutWaitScroll)
}

function getRand(range) {
    [min, max] = range
    return Math.floor(Math.random() * (max - min) + min);
}

async function smoothScroll() {
    let scroll = scroll_element.scrollTop
    while (Math.abs(neededScroll - scroll) > scrollStop) {
        sign = Math.sign(neededScroll - scroll)
        power = (getRand(powerRange) * sign) + scroll
        timeSleep = getRand(sleepRange)
        timeSleep = sleepRange[1]

        scroll_element.scrollTo({top: power, behavior: 'smooth'});
        await new Promise(r => setTimeout(r, timeSleep));
        scroll = scroll_element.scrollTop
    }
    waitScroll()
    scroll_element.scrollTo({top: neededScroll, behavior: 'smooth'});
}

smoothScroll()
