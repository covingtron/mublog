;(function () {
    const application = document.getElementById('trihard-app')
    if (!application) {
        return
    }

    const container = document.getElementById('trihard-grid')
    const row_input = document.getElementById('trihard-max-row')
    const column_input = document.getElementById('trihard-max-column')
    const background_color_input = document.getElementById('trihard-background')
    const foreground_color_input = document.getElementById('trihard-foreground')
    const accent_color_input = document.getElementById('trihard-accent')
    const quadrant_classes = ['trihard-west', 'trihard-north', 'trihard-south', 'trihard-east']
    const triangle_states = ['background', 'foreground', 'accent']

    let grid_data = {}

    function update_colors() {
        application.style.setProperty('--trihard-background', background_color_input.value)
        application.style.setProperty('--trihard-foreground', foreground_color_input.value)
        application.style.setProperty('--trihard-accent', accent_color_input.value)
    }

    function render() {
        const row_letter = ((row_input.value || 'A').match(/[A-Za-z]/) || ['A'])[0].toUpperCase()
        const row_count = row_letter.charCodeAt(0) - 64
        const column_count = Math.min(99, Math.max(1, parseInt(column_input.value, 10) || 1))

        row_input.value = row_letter
        column_input.value = column_count
        container.style.gridTemplateColumns = `repeat(${column_count}, 40px)`
        container.replaceChildren()

        for (let row_index = 0; row_index < row_count; row_index++) {
            for (let column_index = 0; column_index < column_count; column_index++) {
                const position =
                    String.fromCharCode(65 + row_index) + String(column_index + 1).padStart(2, '0')
                grid_data[position] ??= Array(4).fill('background')

                const square = document.createElement('div')
                square.className = 'trihard-position'
                square.title = position

                quadrant_classes.forEach((quadrant, quadrant_index) => {
                    const triangle = document.createElement('div')
                    const current_state = () => grid_data[position][quadrant_index]

                    triangle.className = `trihard-triangle ${quadrant} trihard-${current_state()}`
                    triangle.onclick = (event) => {
                        event.stopPropagation()
                        const state_index =
                            (triangle_states.indexOf(current_state()) + 1) % triangle_states.length
                        const next_state = triangle_states[state_index]

                        grid_data[position][quadrant_index] = next_state
                        triangle.className = `trihard-triangle ${quadrant} trihard-${next_state}`
                        console.log(
                            `Updated ${position} quadrant ${quadrant} to ${next_state}. ` +
                                `Square state: ${grid_data[position].join(',')}`,
                        )
                    }
                    square.appendChild(triangle)
                })
                container.appendChild(square)
            }
        }
    }

    row_input.oninput = render
    column_input.oninput = render
    background_color_input.oninput = update_colors
    foreground_color_input.oninput = update_colors
    accent_color_input.oninput = update_colors

    update_colors()
    render()
})()
