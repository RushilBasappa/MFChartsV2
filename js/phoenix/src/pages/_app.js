import "../styles/globals.css";
import { AuthContextProvider } from "../components";
import { useRouter } from "next/router";
import { ProtectedRoute } from "../components";

const noAuthRequired = ["/login", "/signup"];

function MyApp({ Component, pageProps }) {
  const router = useRouter();
  return (
    <AuthContextProvider>
      {noAuthRequired.includes(router.pathname) ? (
        <Component {...pageProps} />
      ) : (
        <ProtectedRoute>
          <Component {...pageProps} />
        </ProtectedRoute>
      )}
    </AuthContextProvider>
  );
}

export default MyApp;
