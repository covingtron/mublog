;(function () {
    const container = document.getElementById('grid-container')
    const rows_input = document.getElementById('grid-rows')
    const columns_input = document.getElementById('grid-cols')
    const background_color_input = document.getElementById('color-bg')
    const foreground_color_input = document.getElementById('color-fg')
    const accent_color_input = document.getElementById('color-ac')
    const application = document.getElementById('trihard-app')

    let grid_data = {}

    function update_colors() {
        application.style.setProperty('--color-b', background_color_input.value)
        application.style.setProperty('--color-f', foreground_color_input.value)
        application.style.setProperty('--color-a', accent_color_input.value)
    }

    function render() {
        const row_count = Math.min(26, Math.max(1, parseInt(rows_input.value, 10) || 1))
        const column_count = Math.min(99, Math.max(1, parseInt(columns_input.value, 10) || 1))

        container.style.gridTemplateColumns = `repeat(${column_count}, 40px)`
        container.innerHTML = ''

        for (let row_index = 0; row_index < row_count; row_index++) {
            for (let column_index = 0; column_index < column_count; column_index++) {
                const position =
                    String.fromCharCode(65 + row_index) + String(column_index + 1).padStart(2, '0')
                if (!grid_data[position]) {
                    grid_data[position] = 'BBBB'
                }

                const square = document.createElement('div')
                square.className = 'square'
                square.title = position

                const directions = ['W', 'N', 'S', 'E']
                directions.forEach((direction, direction_index) => {
                    const triangle = document.createElement('div')
                    const current_state = () => grid_data[position][direction_index]

                    triangle.className = `triangle ${direction} state-${current_state()}`

                    triangle.onclick = (event) => {
                        event.stopPropagation()
                        const state = current_state()
                        const next_state = state === 'B' ? 'F' : state === 'F' ? 'A' : 'B'

                        const state_characters = grid_data[position].split('')
                        state_characters[direction_index] = next_state
                        grid_data[position] = state_characters.join('')

                        triangle.className = `triangle ${direction} state-${next_state}`
                        console.log(
                            `Updated ${position} direction ${direction} to ${next_state}. ` +
                                `Square state: ${grid_data[position]}`,
                        )
                    }
                    square.appendChild(triangle)
                })
                container.appendChild(square)
            }
        }
    }

    rows_input.oninput = render
    columns_input.oninput = render
    background_color_input.oninput = update_colors
    foreground_color_input.oninput = update_colors
    accent_color_input.oninput = update_colors

    update_colors()
    render()
})()
