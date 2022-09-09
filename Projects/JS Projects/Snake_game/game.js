import {update as updateSnake, draw as drawSnake, Snake_speed} from './snake.js'

let lastRenderTime = 0
const gameboard = document.getElementById('gameboard')

function main(currentTime) {
    window.requestAnimationFrame(main)
    const secondsSinceLastRender = (currentTime - lastRenderTime) / 1000
    if (secondsSinceLastRender < 1 / Snake_speed) return

    console.log('Render')
    lastRenderTime = currentTime

    update()
    draw()

}

window.requestAnimationFrame(main)

function update() {
    updateSnake()
}

function draw() {
    drawSnake()
}