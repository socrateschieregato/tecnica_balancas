import React, { Component } from "react";
import PropTypes from "prop-types";
class Form extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired
  };
  state = {
    cpf_cnpj: "",
    ie: "",
    nome_razao: "",
    nome_fantasia: "",
    email: "",
    im: "",
    // dt_criacao: "",
    grupo: "",
  };
  handleChange = e => {
    this.setState({ [e.target.cpf_cnpj]: e.target.value });
  };
  handleSubmit = e => {
    e.preventDefault();
    const { cpf_cnpj, ie, nome_razao, nome_fantasia, email, im, grupo,} = this.state;
    const empresa = { cpf_cnpj, ie, nome_razao, nome_fantasia, email, im, grupo };
    const conf = {
      method: "post",
      body: JSON.stringify(empresa),
      headers: new Headers({ "Content-Type": "application/json" })
    };
    fetch(this.props.endpoint, conf).then(response => console.log(response));
  };
  render() {
    const { cpf_cnpj, ie, nome_razao, nome_fantasia, email, im, grupo } = this.state;
    return (
      <div className="column">
        <form onSubmit={this.handleSubmit}>
          <div className="field">
            <label className="label">cpf_cnpj</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="cpf_cnpj"
                onChange={this.handleChange}
                value={cpf_cnpj}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">Email</label>
            <div className="control">
              <input
                className="input"
                type="email"
                name="email"
                onChange={this.handleChange}
                value={email}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">ie</label>
            <div className="control">
              <textarea
                className="input"
                type="text"
                name="ie"
                onChange={this.handleChange}
                value={ie}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">nome_razao</label>
            <div className="control">
              <textarea
                className="input"
                type="text"
                name="nome_razao"
                onChange={this.handleChange}
                value={nome_razao}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">nome_fantasia</label>
            <div className="control">
              <textarea
                className="input"
                type="text"
                name="nome_fantasia"
                onChange={this.handleChange}
                value={nome_fantasia}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">IM</label>
            <div className="control">
              <textarea
                className="input"
                type="text"
                name="im"
                onChange={this.handleChange}
                value={im}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">Grupo</label>
            <div className="control">
              <textarea
                className="input"
                type="text"
                name="grupo"
                onChange={this.handleChange}
                value={grupo}
                required
              />
            </div>
          </div>
          <div className="control">
            <button type="submit" className="button is-info">
              Gravar
            </button>
          </div>
        </form>
      </div>
    );
  }
}
export default Form;