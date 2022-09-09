export const Snake_speed = 1
const snakeBody = [{x: 11, y: 11}]

export function update() {
    console.log('update snake')
}

export function draw(gameboard) {
    snakeBody.forEach(segment => {
        const snakeElement = document.createElement('div')
        snakeElement.style.gridRowStart = segment.x
        snakeElement.style.gridColumnStart = segment.y
        snakeElement.classList.add('snake')
        gameboard.appendChild(snakeElement)

    })
    console.log('draw snake')
}