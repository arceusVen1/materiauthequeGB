import React, { PureComponent } from 'react';
import { connect } from 'react-redux';

import { requestMateriaux } from "../../../reducers/materiaux/materiaux.action"

class MateriauxList extends PureComponent {
    constructor(props) {
        super(props);
        this.onClick = this.onClick.bind(this);
        this.state = {
            showList: false,
        };
    }

    makeMateriauxList() {
        const materiauxList = []
        this.props.materiaux.forEach(
            materiau => {
                const item = (
                    <div>
                        <p>
                            {materiau.id}
                        </p>
                        <p>
                            {materiau.nom}
                        </p>
                    </div>
                )
                materiauxList.push(item)
            }
        )
        return materiauxList[0]
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
        return <div>
            <p>{this.props.error}</p>
            <button onClick={this.onClick}>{!this.state.showList ? 'show list' : 'hide list'}</button>
            {this.state.showList && this.makeMateriauxList}
        </div>
    }
}

const mapStateToProps = (materiaux) => ({
    loading: materiaux.loading,
    materiaux: materiaux.materiaux,
    error: materiaux.error,
});

const mapDispatchToProps = {
    requestMateriaux,
};

export default MateriauxList;

export const MateriauxListContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(MateriauxList);
