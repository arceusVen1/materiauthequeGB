import React, { PureComponent } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import { requestMateriaux } from "../../../reducers/materiaux/materiaux.action"
import ListDisplay from '../../tools/ListDisplay';

class MateriauxList extends PureComponent {
    constructor(props) {
        super(props);
        this.onClick = this.onClick.bind(this);
        this.state = {
            showList: false,
        };
    }

    onClick() {
        if (!this.state.showList) {
            this.setState({
                showList: true,
            });
            this.props.requestMateriaux();
        }
        else {
            this.setState({
                showList: false,
            });
        }
    }

    render() {
        const { error, loading, listMateriaux } = this.props;
        return <div>
            <p>{error}</p>
            <p>{loading ? 'chargement' : ''}</p>
            <button onClick={this.onClick}>{!this.state.showList ? 'show list' : 'hide list'}</button>
            {this.state.showList && <ListDisplay list={listMateriaux}/>}
        </div>
    }
}

MateriauxList.PropTypes = {
    error: PropTypes.object,
    loading: PropTypes.bool,
    listMateriaux: PropTypes.array,
    requestMateriaux: PropTypes.func.isRequired,
};

const mapStateToProps = (state) => ({
    loading: state.materiaux.materiaux.loading,
    listMateriaux: state.materiaux.materiaux.listMateriaux,
    error: state.materiaux.materiaux.error,
});

const mapDispatchToProps = {
    requestMateriaux,
};

export default MateriauxList;

export const MateriauxListContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(MateriauxList);
