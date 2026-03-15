;(() => {
    const app = document.getElementById('trihard-app')
    if (!app) {
        return
    }

    const grid = document.getElementById('trihard-grid')
    const maxRowInput = document.getElementById('trihard-max-row')
    const maxColumnInput = document.getElementById('trihard-max-column')
    const colorInputs = {
        accent: document.getElementById('trihard-accent'),
        background: document.getElementById('trihard-background'),
        foreground: document.getElementById('trihard-foreground'),
    }
    const triangleClasses = ['trihard-west', 'trihard-north', 'trihard-south', 'trihard-east']
    const triangleStates = ['background', 'foreground', 'accent']
    const squareStatesByAddress = {}

    const clamp = (value, minimum, maximum) => Math.min(maximum, Math.max(minimum, value))
    const columnLabel = (index) => String(index + 1).padStart(2, '0')
    const rowLabel = (index) => String.fromCharCode(65 + index)
    const squareAddress = (rowIndex, columnIndex) =>
        `${rowLabel(rowIndex)}${columnLabel(columnIndex)}`
    const squareState = (address) =>
        (squareStatesByAddress[address] ??= Array(4).fill('background'))
    const rowCount = () => {
        const letter = ((maxRowInput.value || 'A').match(/[A-Za-z]/) || ['A'])[0].toUpperCase()
        maxRowInput.value = letter
        return letter.charCodeAt(0) - 64
    }

    function setColors() {
        Object.entries(colorInputs).forEach(([name, input]) =>
            app.style.setProperty(`--trihard-${name}`, input.value),
        )
    }

    function cycleTriangle(address, triangleIndex, triangle) {
        const nextStateIndex =
            (triangleStates.indexOf(squareState(address)[triangleIndex]) + 1) %
            triangleStates.length
        squareState(address)[triangleIndex] = triangleStates[nextStateIndex]
        triangle.className = `trihard-triangle ${triangleClasses[triangleIndex]} trihard-${triangleStates[nextStateIndex]}`
    }

    function triangle(address, triangleIndex) {
        const element = document.createElement('div')
        element.className =
            `trihard-triangle ${triangleClasses[triangleIndex]} ` +
            `trihard-${squareState(address)[triangleIndex]}`
        element.onclick = () => cycleTriangle(address, triangleIndex, element)
        return element
    }

    function square(rowIndex, columnIndex) {
        const address = squareAddress(rowIndex, columnIndex)
        const element = document.createElement('div')
        element.className = 'trihard-square'
        element.title = address
        triangleClasses.forEach((_, triangleIndex) =>
            element.appendChild(triangle(address, triangleIndex)),
        )
        return element
    }

    function render() {
        const rows = rowCount()
        const columns = clamp(Number.parseInt(maxColumnInput.value, 10) || 1, 1, 99)
        maxColumnInput.value = columns
        grid.style.gridTemplateColumns = `repeat(${columns}, 40px)`
        grid.replaceChildren(
            ...Array.from({length: rows * columns}, (_, index) =>
                square(Math.floor(index / columns), index % columns),
            ),
        )
    }

    Object.values(colorInputs).forEach((input) => {
        input.oninput = setColors
    })
    maxRowInput.oninput = render
    maxColumnInput.oninput = render

    setColors()
    render()
})()
