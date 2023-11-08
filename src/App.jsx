function App() {
    const posts = [
        {
            title: "React Tailwind Card with Grid 1",
            img: "https://cdn.pixabay.com/photo/2019/12/17/14/43/christmas-4701783__340.png",
            content: "react tailwind css card with image It is a long established fact that a reader will be distracted by the readable content"
        },
        {
            title: "React Tailwind Card with Grid 2",
            img: "https://cdn.pixabay.com/photo/2019/12/17/14/43/christmas-4701783__340.png",
            content: "react tailwind css card with image It is a long established fact that a reader will be distracted by the readable content"
        },
        {
            title: "React Tailwind Card with Grid 3",
            img: "https://cdn.pixabay.com/photo/2019/12/17/14/43/christmas-4701783__340.png",
            content: "react tailwind css card with image It is a long established fact that a reader will be distracted by the readable content"
        },
        {
            title: "React Tailwind Card with Grid 4",
            img: "https://cdn.pixabay.com/photo/2019/12/17/14/43/christmas-4701783__340.png",
            content: "react tailwind css card with image It is a long established fact that a reader will be distracted by the readable content"
        },
    ];
  return (
    <>
      <div className="grid gap-2 lg:grid-cols-4">
          {posts.map((items, key) => (
              <div className="w-full rounded-lg shadow-md lg:max-w-sm" key={key}>
                  <img
                      className="object-cover w-full h-48"
                      src={items.img}
                      alt="image"
                  />
                  <div className="p-4">
                      <h4 className="text-xl font-semibold text-blue-600">
                          
                          {items.title}
                      </h4>
                      <p className="mb-2 leading-normal">
                      {items.content}
                      </p>
                      <button className="px-4 py-2 text-sm text-blue-100 bg-blue-500 rounded shadow">
                          Read more
                      </button>
                  </div>
              </div>
          ))}
      </div>

      <div className="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
          <a href="#">
              <img className="rounded-t-lg" src="/docs/images/blog/image-1.jpg" alt="" />
          </a>
          <div className="p-5">
              <a href="#">
                  <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Noteworthy technology acquisitions 2021</h5>
              </a>
              <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.</p>
              <a href="#" className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                  Read more
              </a>
          </div>
      </div>

    </>
  );
}

export default App
