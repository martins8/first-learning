import './styles.css'

export function Nome(props){
    return (
        <div className="nome">
            <p>
              aluno: <strong>{props.nome}</strong>, idade: <strong>{props.idade}</strong>
            </p>
        </div>
    );
}