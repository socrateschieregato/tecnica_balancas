import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Form from "./Form";


const App = () => (
    <React.Fragment>
        <DataProvider endpoint="v1/empresas/"
                    render={data => <Table data={data}/>}/>
        <Form endpoint="v1/empresas/" />
    </React.Fragment>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
