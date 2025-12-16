function calculateArea(shape, dimensions) {
    switch (shape.toLowerCase()) {
        case 'circle':
            return Math.PI * Math.pow(dimensions.radius, 2);
        case 'square':
            return Math.pow(dimensions.side, 2);
        case 'rectangle':
            return dimensions.length * dimensions.width;
        case 'triangle':
            return 0.5 * dimensions.base * dimensions.height;
        case 'trapezoid':
            return 0.5 * (dimensions.base1 + dimensions.base2) * dimensions.height;
        default:
            return null;
    }
}

function validateDimensions(shape, dimensions) {
    switch (shape.toLowerCase()) {
        case 'circle':
            return dimensions.radius > 0;
        case 'square':
            return dimensions.side > 0;
        case 'rectangle':
            return dimensions.length > 0 && dimensions.width > 0;
        case 'triangle':
            return dimensions.base > 0 && dimensions.height > 0;
        case 'trapezoid':
            return dimensions.base1 > 0 && dimensions.base2 > 0 && dimensions.height > 0;
        default:
            return false;
    }
}

function formatArea(area) {
    return area ? area.toFixed(2) : 'Invalid shape or dimensions';
}

export { calculateArea, validateDimensions, formatArea };