const app = document.getElementById("app");
const root = ReactDOM.createRoot(app);


function Header(props) {
    console.log(props.title)
    return <h1>I am currently using {props.title}</h1>
}






function HomePage() {
    const names = ["React", "HTML", "JS", "C", "C#", "Python"]
    const [likes, setLikes] = React.useState(0);




    function handleClick() {
        setLikes(likes + 1);
    }


    return <div>
        <Header title="React" />
        <ul>
            {names.map((name) => (
                <li key={name}>{name}</li>
            ))}
        </ul>
        <button onClick={handleClick}>Like {likes}</button>
    </div>


}


root.render(<HomePage />);
