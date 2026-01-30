'use client';
import LikeButton from "./like-button";
function Header(props: { title: string }) {
  console.log(props.title);
  return <h1>I am currently using {props.title}</h1>;
}



export default function Home() {
  const names = ["React", "HTML", "JS", "C", "C#", "Python"];


  return (
    <div>
      <Header title="React" />
      <ul>
        {names.map((name) => (
          <li key={name}>{name}</li>
        ))}
      </ul>
      <LikeButton/>
    </div>
  );
}

