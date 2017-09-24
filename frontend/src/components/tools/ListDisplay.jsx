import React, { PureComponent } from 'react';
import PropTypes from 'prop-types';
import ListElement from './ListElement';

class ListDisplay extends PureComponent {

    render() {

        return (<ul>{this.props.list.map((item, index) => (
            <ListElement key={item.id} id={item.id} nom={item.nom}/>
            ))}
            </ul>);
    }
}

ListDisplay.propTypes = {
    list: PropTypes.array,
};

export default ListDisplay;