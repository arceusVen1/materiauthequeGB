import React, { PureComponent } from 'react';
import PropTypes from 'prop-types';

class ListElement extends PureComponent {

    render() {
        return <li>#: {this.props.id}, nom: {this.props.nom}</li>
    }
}

ListElement.propTypes = {
    id: PropTypes.number,
    nom: PropTypes.string,
};

export default ListElement;